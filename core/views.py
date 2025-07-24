from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from .models import Snippet
from .serializers import SnippetSerializer,SimpleSnippetSerializer

class SnippetViewSet(ModelViewSet):
    queryset = Snippet.objects.all()
    lookup_field = 'slug'
    def get_serializer_class(self):
        if self.action == 'list':
            return SimpleSnippetSerializer
        return SnippetSerializer
    @action(detail=True, methods=["post"])
    def view_snippet(self, request, slug=None):
        snippet = self.get_object()
        serializer = self.get_serializer(snippet, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)
