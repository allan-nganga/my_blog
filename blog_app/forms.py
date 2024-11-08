from django import forms

class PostForm(forms.Form):
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