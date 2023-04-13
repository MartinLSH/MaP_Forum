from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from ..models import Post, Category
from ..forms import PostForm

@login_required(login_url='users:login')
def create(request, category_name):
    category = Category.objects.get(name=category_name)
    if len(request.POST.getlist('notice')) == 0:
        notice = False
    else: 
        notice = True
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.create_date = timezone.now()
            post.notice = notice
            post.category = category
            post.save()
            return redirect(category)
    else:
        form = PostForm()
    context = {'form': form, 'category': category}
    return render(request, 'board/post_form.html', context)

@login_required(login_url='users:login')
def modify(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if len(request.POST.getlist('notice')) == 0:
        notice = False
    else: 
        notice = True
    if request.user != post.author:
        messages.error(request, '자신의 글만 수정 가능합니다.')
        return redirect('board:detail', post_id=post.id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.modify_date = timezone.now()  # 수정일시 저장
            post.notice = notice
            post.save()
            return redirect('board:detail', post_id=post.id)
    else:
        form = PostForm(instance=post)
    context = {'form': form, 'category': post.category}
    return render(request, 'board/post_form.html', context)

@login_required(login_url='users:login')
def post_delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.user != post.author and not request.user.is_staff:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('board:detail', post_id=post.id)
    post.delete()
    return redirect('board:index')

@login_required(login_url='common:login')
def vote(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.user == post.author:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        post.voter.add(request.user)
    return redirect('board:detail', post_id=post.id)