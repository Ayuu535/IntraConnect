from django.urls import path
from .views import VoteView

urlpatterns = [
    path('<int:post_id>/', VoteView.as_view()),
]