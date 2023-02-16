from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView, ListView
from blog.models import Post, Category, PostReview
from blog.forms import PostReviewForm
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class HomeView(View):
    def get(self, request):
        new_posts = Post.objects.all()
        popular_posts = Post.objects.all()
        categories = Category.objects.all()
        search_query = request.GET.get('q', '')
        if search_query:
            new_posts = Post.objects.filter(title__icontains=search_query)
            popular_posts = Post.objects.filter(title__icontains=search_query)
        context = {
            'new_posts': new_posts,
            'popular_posts': popular_posts,
            'categories': categories,
            'search_query': search_query
        }
        
        return render(request, 'blog/home.html', context=context)
    
# class PostDetailView(View):
#     def get(self, request, slug):
#         post = Post.objects.get(slug=slug)
#         return render(request, 'blog/post_detail.html', context={'post': post})

# class HomeView(ListView):
#     model = Post
#     template_name = 'blog/home.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['new_posts'] = Post.objects.all() 
#         context['popular_posts'] = Post.objects.all()
#         context['categories'] = Category.objects.all()
#         return context
    
class PostDetailView(View):
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        comments = post.comments.all().order_by('-created_at')
        review_form = PostReviewForm()
        context = {
            'post': post,
            'comments': comments,
            'form': review_form
        }
        return render(request, 'blog/post_detail.html', context=context)
    
class BlogsView(ListView):
    model = Post
    template_name = 'blog/blogs.html'
    context_object_name = 'blogs'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blogs = Post.objects.all().order_by('-published_at')
        paginator = Paginator(blogs, 2)
        page_num = self.request.GET.get('page', 1)
        page_obj = paginator.get_page(page_num)
        context['blogs'] = page_obj
        context['paginator'] = paginator
        return context
    
class AddReviewPostView(LoginRequiredMixin, View):
    def post(self, request, slug):
        post = Post.objects.get(slug=slug)
        post_review = PostReviewForm(data=request.POST)
        
        if post_review.is_valid():
            PostReview.objects.create(post=post, user=request.user, comment=post_review.cleaned_data['comment'])
            return redirect(reverse('blog:post_detail', kwargs={'slug': slug}))
        else:
            comments = post.comments.all().order_by('-created_at')
            context = {
                'post': post,
                'comments': comments,
                'form': post_review
            }
            return render(request, 'blog/post_detail.html', context=context)
        