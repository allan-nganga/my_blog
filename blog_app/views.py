from django.http import JsonResponse
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
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
            return JsonResponse({"message": "Your post was created successfully!", "status": "success"}, status=200)
            # return redirect('post_list')    # Redirect to the homepage after saving
        else:
            return JsonResponse({"message": "There was an error with your submission.", "status":"error"}, status=400)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form':form})

# Delete post Function
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        post.delete()
        messages.success(request, "The post has been deleted successfully")
        return redirect('post_list')
    return render(request, 'blog/post_confirm_delete.html', {'post':post})