from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views import View

from users.forms import UserRegisterForm, UserUpdateForm

# from django.contrib.auth.models import User

# Create your views here.
class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'users/register.html', context={'form': form})
    def post(self, request):
        form = UserRegisterForm(data=request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('users:login')
        else:
            return render(request, 'users/register.html', context={'form': form})
        
    
class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'users/login.html', {'form': form})
    
    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('blog:home')
            else:
                form = AuthenticationForm()
                messages.error(request,"Invalid username or password.")
                return render(request, 'users/login.html', {'form': form})

        else:
            form = AuthenticationForm()
            return render(request, 'users/login.html', {'form': form})

class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.info(request, "You have succesfule logged out.")
        return redirect('blog:home')


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('users:login')
        return render(request, 'users/profile.html', {'user': request.user})
    
    
class ProfileUpdateView(LoginRequiredMixin, View):
    def get(self, request):
        user_update_form = UserUpdateForm(instance=request.user)

        return render(request, 'users/profile.html', {'user': request.user, 'user_form': user_update_form })
    def post(self, request):
        user_update_form = UserUpdateForm(instance=request.user, data=request.POST, files=request.FILES)
        
        if user_update_form.is_valid():
            user_update_form.save()
            return redirect('users:profile-edit')
        else:
            user_update_form = UserUpdateForm(instance=request.user)
            return render(request, 'users/profile.html', {'user': request.user, 'user_form': user_update_form })
