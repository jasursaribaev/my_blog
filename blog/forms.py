from django import forms
from blog.models import PostReview

class PostReviewForm(forms.ModelForm):
    class Meta:
        model = PostReview
        fields = ['comment']
        widgets={"comment":forms.Textarea(attrs={'placeholder':'Comment','name':'comment','class':'comment-text'}),}      
    