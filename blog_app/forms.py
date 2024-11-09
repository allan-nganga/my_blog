from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    title = forms.CharField(
        label="Title", 
        max_length=200,
        required=True,
        error_messages={'required': 'Title is required'}    # Custom error message
    )
    content = forms.CharField(
        label="Content", 
        widget=forms.Textarea
    )

    class Meta:
        model = Post
        fields = ['title', 'content']