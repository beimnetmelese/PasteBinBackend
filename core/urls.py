from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import SnippetViewSet

router = DefaultRouter()
router.register(r'snippets', SnippetViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
