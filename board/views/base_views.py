from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from ..models import Post, Category
from django.db.models import Q, Count
from datetime import datetime, timedelta

def index(request, category_name='free'):
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '') 
    post_list = Post.objects.order_by('-create_date')
    filter = request.GET.get('search_filter', '')
    so = request.GET.get('so','recent')
    
    category_list = Category.objects.all()
    category = get_object_or_404(Category, name=category_name)
    post_list = Post.objects.filter(category=category)
    post_notice = post_list.filter(notice=True)
    
    if so == "recommend":
        post_list = post_list.annotate(num_voter = Count('voter')).order_by("-num_voter","-create_date")
    elif so == "popular":
        post_list = post_list.annotate(num_comment = Count('comment')).order_by("-num_comment","-create_date")
    elif so == "viewed":
        post_list = post_list.order_by("-view_cnt","-create_date")
    else:
        post_list = post_list.order_by("-create_date")
    post_notice = post_notice.order_by("-create_date")
    
    if kw:
        if filter == "title":
            post_list = post_list.filter(
                Q(subject__icontains=kw)
            ).distinct()
        elif filter == "content":
            post_list = post_list.filter(
                Q(content__icontains=kw)
            ).distinct()
        elif filter == "contle":
            post_list = post_list.filter(
                Q(subject__icontains=kw) | 
                Q(content__icontains=kw) 
            ).distinct()
        elif filter == "author":
            post_list = post_list.filter(
                Q(author__username__icontains=kw)
            ).distinct()
        elif filter == "comment":
            post_list = post_list.filter(
                Q(comment__content__icontains=kw)
            ).distinct()
        else:
            post_list = post_list.filter(
                Q(subject__icontains=kw) |  # 제목 검색
                Q(content__icontains=kw) |  # 내용 검색
                Q(comment__content__icontains=kw) |  # 답변 내용 검색
                Q(author__username__icontains=kw)  # 질문 글쓴이 검색
            ).distinct()
    paginator = Paginator(post_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    
    context = {'post_list': page_obj, 'page': page, 'kw': kw, "post_notice":post_notice, 'category_list': category_list, "so":so, 'category': category}
    return render(request, 'board/list.html', context)

def detail(request, post_id):
    post = Post.objects.get(id=post_id)
    category = post.category.name
    context = {'post': post, 'category': category}
    response = render(request, 'board/detail.html', context)
    
    expire_date, now = datetime.now(), datetime.now()
    expire_date += timedelta(days=1)
    expire_date = expire_date.replace(hour=0, minute=0, second=0, microsecond=0)
    expire_date -= now
    max_age = expire_date.total_seconds()
    
    cookie_value = request.COOKIES.get('viewcnt', '_')
    
    if f'_{post_id}_' not in cookie_value:
        cookie_value += f'{post_id}_'
        response.set_cookie('viewcnt', value=cookie_value, max_age=max_age, httponly=True)
        post.view_cnt += 1
        post.save()
        
    return response