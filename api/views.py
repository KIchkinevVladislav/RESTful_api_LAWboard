from requests import Response
from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Post, Comment, Follow, Group
from .serializers import PostSerializer, CommentSerializer, FollowSerializer, GroupSerializer
from .permissions import OwnResoursePermission


class PerformCreateMixsin:
    """
    Overriding perform_create function to save the requesting user as the author.
    """
    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)

    
class PostViewSet(viewsets.ModelViewSet, PerformCreateMixsin):
    """
    Implemented:
    - post creation
    - editing publications
    - get all posts
    - get a separate post
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [OwnResoursePermission, permissions.IsAuthenticatedOrReadOnly]
    
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['group',]

    
class CommentViewSet(viewsets.ModelViewSet, PerformCreateMixsin):
    """
    Implemented:
    - get all comments of a post
    - create a new comment
    - editing publications
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permissions = [OwnResoursePermission, permissions.IsAuthenticatedOrReadOnly]
    
    def list(self, request, post_pk):
        comments = Comment.objects.filter(post=post_pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    
class FollowingViewSet(viewsets.ModelViewSet):
    """
    Implemented:
    - getting a list of all subscribers
    - create a subscription
    """
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filter_backends = [filters.SearchFilter]
    search_fields = ['=user__username', '=following__username']

    
class GroupViewSet(viewsets.ModelViewSet, PerformCreateMixsin):
    """
    Implemented:
    - getting a list of all groups
    - to create a group
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  
