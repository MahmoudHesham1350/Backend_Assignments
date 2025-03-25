from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostForm, commentForm

# View to list all posts
def listPosts(request):
    posts = Post.objects.all()  # Retrieve all posts from the database
    return render(request, 'list_posts.html', {'posts': posts})

# View to display a single post and its comments
def listPost(request, pk):
    post = get_object_or_404(Post, pk=pk)  # Get the post by ID, or return 404 if not found
    comments = post.comments.all()  # Get all comments related to the post
    form = commentForm()  # Instantiate an empty comment form
    
    if request.method == 'POST':  # Check if form is submitted
        if request.user.is_authenticated:  # Ensure user is logged in before posting a comment
            form = commentForm(request.POST)
            if form.is_valid():
                Comment.objects.create(
                    post=post,  # Associate comment with the post
                    user=request.user,  # Assign the logged-in user to the comment
                    comment=form.cleaned_data['comment']  # Save the validated comment text
                )
                return redirect('listPost', pk=post.pk)  # Redirect to the same post page after submission
            
    return render(request, 'list_post.html', {'post': post, 'comments': comments, 'form': form})

# View to update a comment
def commentUpdate(request, pk):
    comment = get_object_or_404(Comment, pk=pk)  # Get the comment by ID, or return 404 if not found
    
    if request.method == 'POST':  # Check if form is submitted
        form = commentForm(request.POST)
        if form.is_valid():
            comment.comment = form.cleaned_data['comment']  # Update comment content
            comment.save()  # Save changes to the database
            return redirect('listPost', pk=comment.post.pk)  # Redirect back to the post page
    else:
        form = commentForm(initial={'comment': comment.comment})  # Pre-fill the form with existing comment data

    return render(request, 'comment_form.html', {'form': form, 'post': comment.post})

# View to delete a comment
def commentDelete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)  # Get the comment by ID, or return 404 if not found
    post_id = comment.post.pk  # Store the post ID before deleting the comment
    comment.delete()  # Delete the comment
    return redirect('listPost', pk=post_id)  # Redirect back to the post page

# View to create a new post
def createPost(request):
    form = PostForm(request.POST or None)  # Initialize form with POST data if available

    if form.is_valid():  # Validate form
        form.save()  # Save the new post to the database
        return redirect('listPosts')  # Redirect to the list of posts

    return render(request, 'create_post.html', {'form': form})  # Render form page

# View to update an existing post
def updatePost(request, pk):
    post = get_object_or_404(Post, pk=pk)  # Get the post by ID, or return 404 if not found
    form = PostForm(request.POST or None, instance=post)  # Initialize form with existing post data

    if form.is_valid():  # Validate form
        form.save()  # Save updated post data to the database
        return redirect('listPosts')  # Redirect to the list of posts

    return render(request, 'create_post.html', {'form': form})  # Render form page

# View to delete a post
def deletePost(request, pk):
    post = get_object_or_404(Post, pk=pk)  # Get the post by ID, or return 404 if not found
    post.delete()  # Delete the post
    return redirect('listPosts')  # Redirect to the list of posts
