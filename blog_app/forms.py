from django import forms
from .models import Post, Comment

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

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4}),
        }