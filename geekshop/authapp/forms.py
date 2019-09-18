import random
import hashlib

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError
from django.forms import forms, HiddenInput, ModelForm

from authapp.models import ShopUser, ShopUserProfile


class ShopUserLoginForm(AuthenticationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ShopUserRegisterForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'password1', 'password2', 'email', 'age', 'genre', 'avatar')

    def __init__(self, *args, **kwargs):
        super(ShopUserRegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError("Вы слишком молоды!")

        return data

    def clean_avatar(self):
        data = self.cleaned_data['avatar']
        if data is not None and data.image.width > 300:
            raise ValidationError("Ширина аватара не должна превышать 300 пикселей.")

        return data

    def save(self):
        user = super(ShopUserRegisterForm, self).save()

        user.is_active = False
        salt = hashlib.sha1(str(random.random()).encode('utf8')).hexdigest()[:6]
        user.activation_key = hashlib.sha1((user.email + salt).encode('utf8')).hexdigest()
        user.save()

        return user


class ShopUserUpdateForm(UserChangeForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'email', 'age', 'genre', 'avatar', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name == 'password':
                field.widget = HiddenInput()

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError("Вы слишком молоды!")

        return data


    def clean_avatar(self):
        data = self.cleaned_data['avatar']
        if data is True and data.image.width > 300:
            raise ValidationError("Ширина аватара не должна превышать 300 пикселей")

        return data


class ShopUserProfileUpdateForm(ModelForm):
    class Meta:
        model = ShopUserProfile
        fields = ('tagline', 'aboutMe', 'gender')

    def __init__(self, *args, **kwargs):
        super(ShopUserProfileUpdateForm, self).__init__(*args, **kwargs)
        for fields_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
