from django.contrib import admin
from blog.models import Profile, Category, PostTag, Post, PostReview, Contact

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'author', 'category', 'is_featured')
    list_filter = ('status', 'author', 'category', 'is_featured')
    prepopulated_fields = {"slug": ("title",)}
    fields = ('title', 'slug', 'body', 'image', 'published_at', 'author', 'category', 'tags', 'is_featured', 'status')

admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(PostTag)
admin.site.register(Post, PostAdmin)
admin.site.register(PostReview)
admin.site.register(Contact)