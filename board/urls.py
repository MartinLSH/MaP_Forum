from django.urls import path

from .views import base_views, post_views, comment_views

app_name = 'board'

urlpatterns = [
    path('', base_views.index, name='index'),
    path('post/list/', base_views.index, name='index'),
    path('post/list/<str:category_name>/', base_views.index, name='index'),
    path('<int:post_id>/', base_views.detail, name='detail'),
    path('comment/create/<int:post_id>/', comment_views.comment_create, name='comment_create'),
    path('post/create/', post_views.create, name='create'),
    path('post/craete/<str:category_name>/', post_views.create, name='create'),
    path('post/modify/<int:post_id>/', post_views.modify, name='modify'),
    path('post/delete/<int:post_id>/', post_views.post_delete, name='post_delete'),
    path('comment/delete/<int:comment_id>/', comment_views.comment_delete, name='comment_delete'),
    path('post/vote/<int:post_id>/', post_views.vote, name='vote'),
]
