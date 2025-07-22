from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseForbidden
from .models import Post, Comment
from django.views.decorators.http import require_POST

# Create your views here.

def index(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts/index.html', {'posts': posts})
    

@login_required
@require_POST
def create_post(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    image = request.FILES.get('image')
    post = Post.objects.create(title=title, content=content, image=image)
    # Ajax 요청이면 JsonResponse 반환
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'result': 'ok'})
    # 일반 폼 제출이면 redirect
    return redirect('index')

@login_required
@require_POST
def toggle_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user
    if user in post.likes.all():
        post.likes.remove(user)
        liked = False
    else:
        post.likes.add(user)
        liked = True
    return JsonResponse({'liked': liked, 'like_count': post.likes.count()})

@login_required
@require_POST
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    content = request.POST.get('content')
    comment = Comment.objects.create(post=post, user=request.user, content=content)
    return JsonResponse({
        'id': comment.id,
        'username': comment.user.username,
        'content': comment.content,
        'created_at': comment.created_at.strftime('%Y-%m-%d %H:%M')
    })

@login_required
@require_POST
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.user != request.user:
        return HttpResponseForbidden()
    comment.delete()
    return JsonResponse({'result': 'ok'})
