from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Q
from .models import Message
from django.contrib.auth.decorators import login_required
# Signup View
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'chat/signup.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, 'chat/signup.html')

        User.objects.create_user(username=username, password=password)
        messages.success(request, "Account created successfully.")
        return redirect('login')

    return render(request, 'chat/signup.html')

# Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('user_list')
        else:
            messages.error(request, "Invalid credentials.")
            return render(request, 'chat/login.html')

    return render(request, 'chat/login.html')

# Logout View
def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('login')

@login_required
def user_list(request):
    users = User.objects.exclude(id=request.user.id)
    return render(request, 'chat/user_list.html', {'users': users})



def chat_view(request, username):
    user = request.user
    other_user = User.objects.get(username=username)

    # Get all messages between the users
    messages = Message.objects.filter(
        (Q(sender=user) & Q(receiver=other_user)) |
        (Q(sender=other_user) & Q(receiver=user))
    ).order_by('timestamp')

    return render(request, 'chat/chat.html', {
        'other_user': other_user,
        'messages': messages,
    })