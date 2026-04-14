from django.urls import path
from .views import PostListCreateView
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')

urlpatterns = router.urls


urlpatterns = [
    path('', PostListCreateView.as_view(), name="posts"),

]