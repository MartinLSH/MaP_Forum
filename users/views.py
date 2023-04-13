from django.contrib.auth import authenticate, login
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from users.forms import UserForm, PasswordResetForm


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'users/signup.html', {'form': form})

class PasswordResetView(auth_views.PasswordResetView):
    """
    비밀번호 초기화 - 사용자ID, email 입력
    """
    template_name = 'users/password_reset.html'
    success_url = reverse_lazy('users:password_reset_done')
    form_class = PasswordResetForm
    # email_template_name = 'users/password_reset_email.html'


class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    """
    비밀번호 초기화 - 메일 전송 완료
    """
    template_name = 'users/password_reset_done.html'


class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    """
    비밀번호 초기화 - 새로운 비밀번호 입력
    """
    template_name = 'users/password_reset_confirm.html'
    success_url = reverse_lazy('users:login')