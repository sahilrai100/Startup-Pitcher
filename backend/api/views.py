from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Idea, Comment, Like
from .serializers import (
    IdeaSerializer, IdeaCreateSerializer, CommentSerializer, 
    LikeSerializer, UserRegistrationSerializer, UserSerializer
)

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.pitcher == request.user

class IdeaViewSet(viewsets.ModelViewSet):
    queryset = Idea.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    
    def get_serializer_class(self):
        if self.action == 'create':
            return IdeaCreateSerializer
        return IdeaSerializer
    
    def perform_create(self, serializer):
        serializer.save(pitcher=self.request.user)
    
    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def like(self, request, pk=None):
        idea = self.get_object()
        user = request.user
        
        like, created = Like.objects.get_or_create(user=user, idea=idea)
        
        if not created:
            # Unlike if already liked
            like.delete()
            return Response({'status': 'unliked'}, status=status.HTTP_200_OK)
        
        return Response({'status': 'liked'}, status=status.HTTP_201_CREATED)
    
    @action(detail=True, methods=['get'])
    def comments(self, request, pk=None):
        idea = self.get_object()
        comments = idea.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        idea_id = self.kwargs.get('idea_pk')
        idea = Idea.objects.get(pk=idea_id)
        serializer.save(commenter=self.request.user, idea=idea)
    
    def get_queryset(self):
        idea_id = self.kwargs.get('idea_pk')
        return Comment.objects.filter(idea_id=idea_id)

class TopIdeasView(APIView):
    permission_classes = [permissions.AllowAny]
    
    def get(self, request):
        top_ideas = Idea.objects.all()[:5]
        serializer = IdeaSerializer(top_ideas, many=True, context={'request': request})
        return Response(serializer.data)

@method_decorator(csrf_exempt, name='dispatch')
class UserRegistrationView(APIView):
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'user': UserSerializer(user).data,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_exempt, name='dispatch')
class UserLoginView(APIView):
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        if not username or not password:
            return Response({'error': 'Please provide both username and password'}, 
                          status=status.HTTP_400_BAD_REQUEST)
        
        user = authenticate(username=username, password=password)
        
        if user:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            return Response({
                'user': UserSerializer(user).data,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            return Response({'error': 'Invalid credentials'}, 
                          status=status.HTTP_401_UNAUTHORIZED)

class UserLogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        logout(request)
        return Response({'message': 'Successfully logged out'}) 