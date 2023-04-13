from django import forms
from board.models import Post, Comment
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['subject', 'content', 'notice']
        widgets = {
            'content': CKEditorUploadingWidget(),
        }
        labels = {
            'subject': '제목',
            'content': '내용',
            'notice': '공지',
        }  
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '답변내용',
        }