from requests import Response
from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend


from .models import Post, Comment, Follow, Group
from .serializers import PostSerializer, CommentSerializer, FollowSerializer, GroupSerializer
from .permissions import OwnResoursePermission

class PerformCreateMixsin:
    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)

class PostViewSet(viewsets.ModelViewSet, PerformCreateMixsin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [OwnResoursePermission, permissions.IsAuthenticatedOrReadOnly]
    
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['group',]

class CommentViewSet(viewsets.ModelViewSet, PerformCreateMixsin):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permissions = [OwnResoursePermission, permissions.IsAuthenticatedOrReadOnly]
    
    def list(self, request, post_pk):
        comments = Comment.objects.filter(post=post_pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

class FollowingViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filter_backends = [filters.SearchFilter]
    search_fields = ['=user__username', '=following__username']

class GroupViewSet(viewsets.ModelViewSet, PerformCreateMixsin):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]





    