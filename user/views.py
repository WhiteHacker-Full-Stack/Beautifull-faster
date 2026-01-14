import random

from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import PasswordForm
from django.template.defaultfilters import title

from .forms import UserRegisterForm
from .models import Profile
from .forms import ProfileForm

# Create your views here.

def register(request):
    title = 'Sign Up'
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            login(request,user)
            return redirect('profile')
        else:
            return HttpResponse("malumot tog'ri emas ")
    form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form,'title':title})

def profile(request):
    title = 'User Profile'
    user = request.user
    try:
        profile = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=user)
    malumot = {
        'user': user,
        'profile': profile,
        'title': title,
    }
    return render(request, 'user/profile.html', malumot)

def profile_edit(request):
    title = 'Profile Edit'
    javob = ""
    profile = Profile.objects.get(user=request.user)
    data = request.POST
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile.ism = data['ism']
            profile.familiya = data['familiya']
            profile.tug_sana = data['tug_sana']
            profile.bio = data['bio']
            profile.nomer = data['nomer']
            profile.foto = request.FILES['foto']
            profile.save()
            return redirect('profile')
        else:
            javob = "oxshamadi"
            return HttpResponse(form.errors, status=400)
    return render(request, 'user/profile_edit.html', {'form': form, 'javob': javob, 'title': title})

def password_change(request):
    title = 'Password Change'
    form = PasswordForm()
    if request.method == 'POST':
        form = PasswordForm( request.POST)
        if form.is_valid():
            password = request.POST['password1']
            request.user.set_password(password)
            user = request.user.save()
            login(request, user)
            return redirect('profile')
    return render(request, 'user/password_change.html', {'title': title, 'form': form})


def password_reset_view(request):
    title = 'Password Reset'
    javob = ""
    if request.method == 'POST':
        data = request.POST
        username = data['username']
        try:
            user = User.objects.get(username=username)
            email = user.email
            code = random.randint(100000, 1000000)
            print(code)
            request.session['code'] = str(code)
            return redirect('verify_view')
        except:
            javob = "Username does not exist"
    return render(request,'user/password_reset.html', {'title': title, 'javob': javob})

def verify_view(request):
    title = 'Verify'
    javob = ""
    if request.method == 'POST':
        data = request.POST
        code = data['code']
        our_code = request.session.get('code')
        if code != our_code:
            javob = "Our code doesn't match"

        else:
            return redirect('password_change2')
    return render(request, 'user/verify_view.html', {'title': title, 'javob': javob})





