from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from account_module.models import User


class RegisterForm(forms.Form):
    name = forms.CharField(
        label='name',
        widget=forms.TextInput(
            attrs={
                'class': 'sign__input',
                'placeholder': 'Username'
            }

        ),
        validators=[

            validators.MaxLengthValidator(100)
        ]
    )

    email = forms.EmailField(
        label='email',
        widget=forms.EmailInput(attrs={
            'class': 'sign__input',
            'placeholder': 'Email'
        }),
        validators=[
            validators.EmailValidator,
            validators.MaxLengthValidator(100)
        ]
    )
    password = forms.CharField(
        label='password',
        widget=forms.PasswordInput(attrs={
            'class': 'sign__input',
            'placeholder': 'Password'
        }),
        validators=[

            validators.MaxLengthValidator(100)
        ]
    )
    confirm_password = forms.CharField(
        label='confirm password',
        widget=forms.PasswordInput(attrs={
            'class': 'sign__input',
            'placeholder': 'Confirm Password'
        }),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password == confirm_password:
            return confirm_password
        raise ValidationError('password with confirm it is not match ')


class LoginForm(forms.Form):
    email = forms.EmailField(
        label='email',
        widget=forms.EmailInput(attrs={
            'class': 'sign__input',
            'placeholder': 'Email'
        }),
        validators=[
            validators.EmailValidator,
            validators.MaxLengthValidator(100)
        ]
    )
    password = forms.CharField(
        label='password',
        widget=forms.PasswordInput(attrs={
            'class': 'sign__input',
            'placeholder': 'Password'
        }),
        validators=[

            validators.MaxLengthValidator(100)
        ]
    )


class EditProfileModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'image', 'address', 'username', 'mobile']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',

            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control'

            }),
            'username': forms.TextInput(attrs={
                'class': 'form-control'

            }),
            'mobile': forms.TextInput(attrs={
                'class': 'form-control'

            })
        }


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(
        label=' old password...',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }),
        validators=[

            validators.MaxLengthValidator(100)
        ]
    )
    new_password = forms.CharField(
        label='new password...',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control'
        }),
        validators=[

            validators.MaxLengthValidator(100)
        ]
    )
    confirm_password = forms.CharField(
        label='confirm password...',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control'
        }),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('new_password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password == confirm_password:
            return confirm_password
        raise ValidationError('password with confirm it is not match ')
