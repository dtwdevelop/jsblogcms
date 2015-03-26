from django.shortcuts import render

from rest_framework import authentication, permissions, viewsets
from blog.models import Category , Page ,Comment
from .serializers import CategorySerializer,PagesSerializer,CommentSerializer
from rest_framework.renderers import JSONRenderer

class DefaultsMixin(object):
    """Default settings for view authentication, permissions,
    filtering and pagination."""
    # authentication_classes = (
    # authentication.BasicAuthentication,
    # authentication.TokenAuthentication,
    # )
    # permission_classes = (
    # permissions.IsAuthenticated,
    # )
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100

class CategoryViewSet(DefaultsMixin,viewsets.ModelViewSet):
    """API endpoint for listing and creating sprints."""
    renderer_classes = [ JSONRenderer]
    queryset = Category.objects.order_by('title_category')
    serializer_class = CategorySerializer

class PagesViewSet(DefaultsMixin,viewsets.ModelViewSet):
    """API endpoint for listing and creating sprints."""
    renderer_classes = [ JSONRenderer]
    queryset = Page.objects.all()
    serializer_class = PagesSerializer

class CommentsViewSet(DefaultsMixin,viewsets.ModelViewSet):
    """API endpoint for listing and creating sprints."""
    renderer_classes = [ JSONRenderer]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

