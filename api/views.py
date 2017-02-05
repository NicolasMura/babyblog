# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from babyblog.models import Post
from serializers import (
    PostDetailSerializer,
    PostCreateSerializer,
    PostSerializer,
    # UserListSerializer,
    # UserDetailSerializer,
    UserSerializer,
)
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import mixins
from rest_framework import status
from rest_framework import permissions
# from snippets.permissions import IsOwnerOrReadOnly, IsAuthenticatedOrCreate

# Imports for endpoint for the root of our ListAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import list_route
from rest_framework.reverse import reverse

# Imports for oauth2_provider
from oauth2_provider.ext.rest_framework import OAuth2Authentication

# Test
from rest_framework.parsers import MultiPartParser, JSONParser
# from rest_framework.parsers import (
#     MultiPartParser, FileUploadParser, JSONParser, FormParser)

from django.contrib.auth.models import User
from django.http import Http404


# REST views
# Endpoint for the root of our ListAPIView
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'profiles': reverse(
            'api:user-list', request=request, format=format),
        'posts': reverse(
            'api:post-list', request=request, format=format),
        'post-create': reverse(
            'api:post-create', request=request, format=format),
        'post-latest': reverse(
            'api:post-latest-detail', request=request, format=format),
    })


class PostAPIViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(parent=None).order_by('-date')

    serializer_class = PostCreateSerializer

    @list_route()
    def roots(self, request):
        queryset = Post.objects.filter(parent=None)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class PostCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.order_by(('-date'))
    serializer_class = PostCreateSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # authentication_classes = [OAuth2Authentication]
    # permission_classes = [TokenHasScope]
    # parser_classes = (
    #     MultiPartParser, FileUploadParser, JSONParser, FormParser)
    parser_classes = (MultiPartParser, JSONParser)

    # # Overriding perform_create() method to associate Posts with Profiles
    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)


class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    # permission_classes = (
    #     permissions.IsAuthenticatedOrReadOnly,
    #     IsOwnerOrReadOnly,
    # )


class PostLatestDetailAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_object(self, *args, **kwargs):
        return self.queryset.latest('date')


# class PostCreate(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostCreateSerializer


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UserDetailAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
