from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')  #Get all posts, ordered by  creation date (newest first)
    return render(request, 'blog/post_list.html', {'posts':posts})

# Function for new post
@login_required
def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({"status": "success", "message": "Your post was created successfully!"})
            messages.success(request, "Your post was created successfully!")
            return redirect('post_detail', pk=post.pk)
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({"status": "error", "message": "There was an error creating your post."})
            messages.error(request, "There was an error creating your post.")
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})

# Delete post Function
@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        post.delete()
        messages.success(request, "The post has been deleted successfully")
        return redirect('post_list')
    return render(request, 'blog/post_confirm_delete.html', {'post':post})

# Edit post function
@login_required
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({"status": "success", "message": "The post has been updated successfully"})
            messages.success(request, "The post has been updated successfully")
            return redirect('post_detail', pk=post.pk)
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({"status": "error", "message": "There was an error updating the post."})
            messages.error(request, "There was an error updating the post.")
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form, 'post': post})

# Post Details function
@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()  # Retrieve all comments for this post

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post # Associate the comment with the current post
            comment.save()
            messages.success(request, "Your comment has been added!")
            return redirect('post_detail', pk=post.pk)
        else:
            messages.error(request, "There was an error submitting your comment!")
    else:
        form = CommentForm()
        
    return render(request, 'blog/post_detail.html', {'post': post, 'comments':comments, 'form': form})