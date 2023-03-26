from django.urls import path, include
from rest_framework_nested import routers
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . views import  PostViewSet, CommentViewSet, FollowingViewSet, GroupViewSet

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
comments_router = routers.NestedDefaultRouter(router, r'posts', lookup='posts')
comments_router.register(r'comments', CommentViewSet, basename='comments')
router.register('follow', FollowingViewSet, basename='follow')
router.register('group', GroupViewSet, basename='group')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(comments_router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ]
