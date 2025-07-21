from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username or not password:
            messages.error(request, '닉네임과 비밀번호를 모두 입력하세요.')
        elif User.objects.filter(username=username).exists():
            messages.error(request, '이미 존재하는 닉네임입니다.')
        else:
            user = User.objects.create_user(username=username, password=password)
            messages.success(request, '회원가입이 완료되었습니다. 로그인 해주세요!')
            return redirect('login')
    return render(request, 'users/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            messages.error(request, '닉네임 또는 비밀번호가 올바르지 않습니다.')
    return render(request, 'users/login.html')

def logout(request):
    auth_logout(request)
    return redirect('login')
