from django.urls import path
from blog.views import HomeView, PostDetailView, BlogsView, AddReviewPostView

app_name = 'blog'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('posts/<slug:slug>', PostDetailView.as_view(), name='post_detail'),
    path('posts/', BlogsView.as_view(), name='all-posts'),
    path('<slug:slug>/reviews/', AddReviewPostView.as_view(), name='reviews'),
]
