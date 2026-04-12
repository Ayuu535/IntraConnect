from django.urls import path
from .views import CommentCreateView, CommentListView

urlpatterns = [
    path('create/', CommentCreateView.as_view()),
    path('<int:post_id>/', CommentListView.as_view()),
]