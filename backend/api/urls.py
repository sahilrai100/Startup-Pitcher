from django.urls import path, include
from rest_framework_nested import routers
from .views import (
    IdeaViewSet, CommentViewSet, TopIdeasView,
    UserRegistrationView, UserLoginView, UserLogoutView
)

router = routers.DefaultRouter()
router.register(r'ideas', IdeaViewSet)

ideas_router = routers.NestedDefaultRouter(router, r'ideas', lookup='idea')
ideas_router.register(r'comments', CommentViewSet, basename='idea-comments')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(ideas_router.urls)),
    path('top-ideas/', TopIdeasView.as_view(), name='top-ideas'),
    path('auth/register/', UserRegistrationView.as_view(), name='register'),
    path('auth/login/', UserLoginView.as_view(), name='login'),
    path('auth/logout/', UserLogoutView.as_view(), name='logout'),
] 