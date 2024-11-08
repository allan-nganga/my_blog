from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

# Create your views here.
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')  #Get all posts, ordered by  creation date (newest first)
    return render(request, 'blog/post_list.html', {'posts':posts})

# Function for new post
def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            # Save the post data to the database
            post = Post(
                title = form.cleaned_data['title'],
                content = form.cleaned_data['content'],
                author = request.user   # Assuming the user is logged in
            )
            post.save()
            return redirect('post_list')    # Redirect to the homepage after saving
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form':form})