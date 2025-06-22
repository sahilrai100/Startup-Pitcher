from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Idea, Comment, Like

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        read_only_fields = ['id']

class CommentSerializer(serializers.ModelSerializer):
    commenter = UserSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = ['id', 'content', 'commenter', 'created_at']
        read_only_fields = ['id', 'commenter', 'created_at']

class IdeaSerializer(serializers.ModelSerializer):
    pitcher = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    is_liked = serializers.SerializerMethodField()
    
    class Meta:
        model = Idea
        fields = ['id', 'title', 'description', 'pitcher', 'created_at', 'updated_at', 'likes_count', 'comments', 'is_liked']
        read_only_fields = ['id', 'pitcher', 'created_at', 'updated_at', 'likes_count', 'is_liked']
    
    def get_is_liked(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.likes.filter(user=request.user).exists()
        return False

class IdeaCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idea
        fields = ['title', 'description']

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'user', 'idea', 'created_at']
        read_only_fields = ['id', 'user', 'created_at']

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_confirm', 'first_name', 'last_name']
    
    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError("Passwords don't match")
        return data
    
    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = User.objects.create_user(**validated_data)
        return user 