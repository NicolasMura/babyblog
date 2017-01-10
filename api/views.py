# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from babyblog.models import Post
from serializers import (
    PostSerializer,
    ProfileSerializer,
)
from rest_framework import generics
# from rest_framework import permissions
# from snippets.permissions import IsOwnerOrReadOnly, IsAuthenticatedOrCreate

# Imports for endpoint for the root of our ListAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, list_route
from rest_framework.reverse import reverse

# Imports for oauth2_provider
# from oauth2_provider.ext.rest_framework import OAuth2Authentication

# Test
from rest_framework.parsers import MultiPartParser, JSONParser
# from rest_framework.parsers import (
#     MultiPartParser, FileUploadParser, JSONParser, FormParser)


from zn_auth.models import Profile


# REST views
# Endpoint for the root of our ListAPIView
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'profiles': reverse(
            'api:profile-list', request=request, format=format),
        'posts': reverse(
            'api:post-list', request=request, format=format)
    })


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all().filter(parent=None).order_by(('-date'))
    serializer_class = PostSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # authentication_classes = [OAuth2Authentication]
    # permission_classes = [TokenHasScope]
    # parser_classes = (
    #     MultiPartParser, FileUploadParser, JSONParser, FormParser)
    parser_classes = (MultiPartParser, JSONParser)

    # Overriding perform_create() method to associate Posts with Profiles
    def perform_create(self, serializer):
        serializer.save(author=self.request.username)

    @list_route()
    def roots(self, request):
        queryset = Post.objects.filter(parent=None)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = (
    #     permissions.IsAuthenticatedOrReadOnly,
    #     IsOwnerOrReadOnly,
    # )


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
