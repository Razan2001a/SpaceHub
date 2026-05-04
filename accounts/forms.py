from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label='البريد الإلكتروني / Email'
    )
    role = forms.ChoiceField(
        choices=UserProfile.Role.choices,
        label='نوع الحساب / Account Type',
        widget=forms.RadioSelect
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'اسم المستخدم / Username',
            'password1': 'كلمة المرور / Password',
            'password2': 'تأكيد كلمة المرور / Confirm Password',
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            user.profile.role = self.cleaned_data['role']
            user.profile.save()
        return user


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=150, required=False,
        label='الاسم الأول / First Name'
    )
    last_name = forms.CharField(
        max_length=150, required=False,
        label='الاسم الأخير / Last Name'
    )

    class Meta:
        model = UserProfile
        fields = ['phone', 'bio', 'profile_pic']
        labels = {
            'phone':       'رقم الهاتف / Phone',
            'bio':         'نبذة عنك / Bio',
            'profile_pic': 'صورة الملف الشخصي / Profile Picture',
        }