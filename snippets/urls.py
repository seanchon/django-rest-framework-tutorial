from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

from django.conf.urls import url, include

from snippets import views


# Tutorial 7: Adding a schema
schema_view = get_schema_view(title='Pastebin API')

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    url(r'^schema/$', schema_view),
    url(r'^', include(router.urls)),
]
