from account.models import CustomUser
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages

# Create your views here.


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(
                request, 'Welcome, <strong>%s</strong>, You Logged in Successfully...' % user.email)
            return redirect('home')
        else:
            messages.error(
                request, 'Invalid Credentials, Please Try Again...')

    context = {}
    return render(request, 'account/login.html', context)


def register_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        re_password = request.POST.get('re-password')

        if password != re_password:
            messages.warning(
                request, 'Password & Confirm Password does not Match')

            context = {'values': request.POST}
            return render(request, 'account/register.html', context)

        CustomUser.objects.create_user(email=email, password=password)
        messages.success(
            request, 'Your Profile has been created Successfully, Now you can Log In.')
        return redirect('login')

    context = {}
    return render(request, 'account/register.html', context)


def logout_view(request):
    auth.logout(request)
    messages.success(request, "You Logged out Successfully")
    return redirect('login')
