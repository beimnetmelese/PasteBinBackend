from rest_framework import serializers
from .models import Snippet
from .utils import encrypt_text, decrypt_text
from django.contrib.auth.hashers import make_password, check_password
from django.utils import timezone

class SimpleSnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['slug', 'language', 'expiry_time', 'one_time_view']

class SnippetSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    plain_text = serializers.CharField(write_only=True)
    decrypted = serializers.SerializerMethodField()

    class Meta:
        model = Snippet
        fields = ['slug', 'plain_text', 'language', 'password', 'expiry_time', 'one_time_view', 'decrypted', "created_at"]
        read_only_fields = ['slug', 'decrypted']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        text = validated_data.pop('plain_text')

        snippet = Snippet(**validated_data)
        snippet.content_encrypted = encrypt_text(text)

        if password:
            snippet.password_hash = make_password(password)

        snippet.save()
        return snippet

    def get_decrypted(self, obj):
        request = self.context.get('request')
        password = request.data.get('password') if request else None

        if obj.is_expired():
            return "This paste has expired."

        if obj.one_time_view and obj.has_been_viewed:
            return "This paste was already viewed (one-time only)."

        # 💡 Check password BEFORE decrypting
        if obj.password_hash:
            if not password or not check_password(password, obj.password_hash):
                return "Password required or incorrect"

        try:
            decrypted = decrypt_text(obj.content_encrypted)
        except Exception:
            return "Decryption failed. Paste may be corrupted or tampered."

        if obj.one_time_view and not obj.has_been_viewed:
            obj.has_been_viewed = True
            obj.save()

        return decrypted

