from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

def blog_index(request):
    posts = Post.objects.order_by('-pub_date')
    return render(request, 'posts/blog_index.html', {'posts': posts})

def post_detail(request, post_id, slug):
    post = get_object_or_404(Post, pk=post_id)
    if slug != post.slug():
        return redirect(post, permanent=True)
    return render(request, 'posts/post_detail.html', {'post': post})
