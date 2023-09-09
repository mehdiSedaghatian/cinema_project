from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from .forms import RegisterForm, LoginForm
from .models import User
from django.contrib.auth import login, logout
from .forms import EditProfileModelForm, ChangePasswordForm
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.utils.decorators import method_decorator


# Create your views here.
class SignUpView(View):
    def get(self, request):
        form = RegisterForm()
        context = {
            'form': form
        }
        return render(request, 'account_module/sign_up_page.html', context)

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user: bool = User.objects.filter(email=email).exists()
            if user:
                form.add_error('email', 'user with this email is exist')
            else:
                new_user = User(username=name, email=email)
                new_user.is_active = True
                new_user.set_password(password)
                new_user.save()
                return redirect(reverse('sign_in'))



        else:
            context = {
                'form': form
            }
            return render(request, 'account_module/sign_up_page.html', context)


class SignInView(View):
    def get(self, request):
        form = LoginForm()
        context = {
            'form': form
        }
        return render(request, 'account_module/sign_in_page.html', context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user: User = User.objects.filter(email=email).first()
            if user is not None:
                is_password_correct = user.check_password(password)
                if is_password_correct:
                    login(request, user)
                    return redirect(reverse('home_page'))
                else:
                    form.add_error('password', 'your password is wrong')


            else:
                form.add_error('email', 'first sign up ,and next try to sign in')
                return redirect(reverse('sign_up'))




        else:
            context = {
                'form': form
            }
            return render(request, 'account_module/sign_in_page.html', context)


class SignOutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('home_page'))


class Profile(View):
    def get(self, request):
        profile = request.user
        context = {
            'profile': profile
        }
        return render(request, 'account_module/profile_page.html', context)


@method_decorator(login_required, name='dispatch')
class EditUserProfilePage(View):
    def get(self, request: HttpRequest):
        current = User.objects.filter(id=request.user.id).first()
        edit_profile = EditProfileModelForm(instance=current)
        context = {
            'edit_profile': edit_profile,
            'current_user': current
        }

        return render(request, 'account_module/edit_profile_page.html', context)

    def post(self, request: HttpRequest):
        current = User.objects.filter(id=request.user.id).first()
        edit_profile = EditProfileModelForm(request.POST, request.FILES, instance=current)
        if edit_profile.is_valid():
            edit_profile.save(commit=True)
            current = User.objects.filter(id=request.user.id).first()

        context = {
            'edit_profile': edit_profile,
            'current_user': current



        }
        return render(request, 'account_module/edit_profile_page.html', context)


@method_decorator(login_required, name='dispatch')
class ChangePasswordPage(View):
    def get(self, request: HttpRequest):
        change_password_form = ChangePasswordForm()
        context = {
            'change_password_form': change_password_form
        }
        return render(request, 'account_module/change_password.html', context)

    def post(self, request: HttpRequest):
        change_password_form = ChangePasswordForm(request.POST)
        if change_password_form.is_valid():
            current_user: User = User.objects.filter(id=request.user.id).first()
            if current_user.check_password(change_password_form.cleaned_data.get('old_password')):
                current_user.set_password(change_password_form.cleaned_data.get('new_password'))
                current_user.save()
                logout(request)
                return redirect(reverse('sign_in'))



            else:
                change_password_form.add_error('old_password', 'current password is wrong')

        context = {
            'change_password_form': change_password_form
        }
        return render(request, 'account_module/change_password.html', context)
