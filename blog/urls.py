from django.urls import path
# Dodaj api_posts do importów z .views
from .views import PostListView, PostDetailView, api_posts

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    # Nowa ścieżka dla Twojego API JSON
    path('api/json/', api_posts, name='api_posts_json'),
]