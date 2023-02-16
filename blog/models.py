from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User
from users.models import CustomUser

# Create your models here.
STATUS = (
    (0, 'Draft'),
    (1, 'Publish')
)

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    website = models.URLField(max_length=300,blank=True, null=True)
    location = models.CharField(max_length=80, blank=True, null=True)
    bio = models.TextField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   
    def __str__(self):
        return f"{self.user.username}" 
    
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class PostTag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=100)
    body = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField(upload_to='blogs/images')
    is_featured = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(default=timezone.now)
    
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='authors_posts')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')
    tags = models.ManyToManyField(PostTag, blank=True, related_name='tags')
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
    
class PostReview(models.Model):
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.subject