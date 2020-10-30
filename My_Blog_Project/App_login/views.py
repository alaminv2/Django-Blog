from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from App_login.forms import SignUpForms, ChangeProfileForm, ProfilePic
# Create your views here.

def SignUp(request):
    new_form = SignUpForms()
    registered = False
    if request.method == 'POST':
        new_form = SignUpForms(data = request.POST)
        if new_form.is_valid():
            new_form.save()
            registered = True
    context = {
        'registered' : registered,
        'new_form' : new_form,
    }
    return render(request, 'App_login/sign_up.html', context=context)


def UserLogin(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
    return render(request, 'App_login/login.html', context={'form' : form})

@login_required
def UserLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def UserProfile(request):
    return render(request, 'App_login/user_profile.html', context={})


@login_required
def UserChangeProfile(request):
    current_user = request.user
    form = ChangeProfileForm(instance=current_user)
    if request.method == 'POST':
        form = ChangeProfileForm(data=request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            # form = ChangeProfileForm(instance=current_user)
            return UserProfile(request)
    return render(request, 'App_login/change_profile.html', context={'form' : form})

@login_required
def ChangePassword(request):
    changed = False
    current_user = request.user
    form = PasswordChangeForm(current_user)
    if request.method == 'POST':
        form = PasswordChangeForm(current_user, data=request.POST)
        if form.is_valid():
            form.save()
            changed = True
            return UserProfile(request)
    return render(request, 'App_login/change_pass.html', context={'form' : form, 'changed' : changed})


@login_required
def Add_Profile_Pic(request):
    form = ProfilePic()
    if request.method == 'POST':
        form = ProfilePic(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return HttpResponseRedirect(reverse('App_login:user_profile'))
    return render(request, 'App_login/add_pro_pic.html', context={'form' : form})


@login_required
def Change_Profile_Pic(request):
    form = ProfilePic(instance=request.user.user_profile)
    if request.method == 'POST':
        form = ProfilePic(request.POST, request.FILES, instance=request.user.user_profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('App_login:user_profile'))
    return render(request, 'App_login/add_pro_pic.html', context={'form' : form})
