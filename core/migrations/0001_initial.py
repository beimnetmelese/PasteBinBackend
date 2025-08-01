# Generated by Django 5.2.4 on 2025-07-24 09:34

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(default=uuid.uuid4, unique=True)),
                ('content_encrypted', models.TextField()),
                ('language', models.CharField(default='plaintext', max_length=30)),
                ('password_hash', models.CharField(blank=True, max_length=128, null=True)),
                ('expiry_time', models.DateTimeField(blank=True, null=True)),
                ('one_time_view', models.BooleanField(default=False)),
                ('has_been_viewed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
