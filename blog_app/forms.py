from django import forms

class PostForm(forms.Form):
    title = forms.CharField(label="Title", max_length=200)
    content = forms.CharField(label="Content", widget=forms.Textarea)