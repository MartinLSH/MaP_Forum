from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from ..models import Post, Comment
from ..forms import CommentForm

@login_required(login_url='users:login')
def comment_create(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.post = post
            comment.save()
            return redirect('board:detail', post_id=post.id)
    else:
        form = CommentForm()
    context = {'post': post, 'form': form}
    return render(request, 'board/detail.html', context)

@login_required(login_url='users:login')
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author and not request.user.is_staff:
        messages.error(request, '삭제권한이 없습니다')
    else:
        comment.delete()
    return redirect('board:detail', post_id=comment.post.id)