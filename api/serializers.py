from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Post, Comment, Group, Follow, User


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date')
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
        model = Comment

        
class FollowSerializer(serializers.ModelSerializer):
    field = ('user', 'following')
    model = Follow

    def validate(self, data):
        user = self.context['request'].user
        author = data['following']
        follow_user = User.objects.get(username=author['username'])
        get_following = Follow.objects.filter(user=user, following=follow_user)
        data['following'] = follow_user
        if get_following:
            raise ValidationError()
        return data

    
class GroupSerializer(serializers.ModelSerializer):
    field = ('title',)
    model = Group
