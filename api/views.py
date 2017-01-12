# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from babyblog.models import Post
from serializers import (
    PostListSerializer,
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
# from rest_framework import permissions
# from snippets.permissions import IsOwnerOrReadOnly, IsAuthenticatedOrCreate
# from rest_framework import permissions

# Imports for endpoint for the root of our ListAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import list_route
from rest_framework.reverse import reverse

# Imports for oauth2_provider
# from oauth2_provider.ext.rest_framework import OAuth2Authentication

# Test
from rest_framework.parsers import MultiPartParser, JSONParser
# from rest_framework.parsers import (
#     MultiPartParser, FileUploadParser, JSONParser, FormParser)

from django.contrib.auth.models import User


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
            'api:post-create', request=request, format=format)
    })


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(parent=None).order_by('-date')

    serializer_class = PostListSerializer

    @list_route()
    def roots(self, request):
        queryset = Post.objects.filter(parent=None)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.order_by(('-date'))
    serializer_class = PostListSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # authentication_classes = [OAuth2Authentication]
    # permission_classes = [TokenHasScope]
    # parser_classes = (
    #     MultiPartParser, FileUploadParser, JSONParser, FormParser)
    parser_classes = (MultiPartParser, JSONParser)

    # # Overriding perform_create() method to associate Posts with Profiles
    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    # permission_classes = (
    #     permissions.IsAuthenticatedOrReadOnly,
    #     IsOwnerOrReadOnly,
    # )


class PostCreate(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
