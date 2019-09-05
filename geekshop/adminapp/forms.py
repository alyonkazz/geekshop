from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms import forms, ModelForm

from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product


class ShopUserAdminCreateForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'password1', 'password2',
                  'email', 'age', 'avatar')

    def __init__(self, *args, **kwargs):
        super(ShopUserAdminCreateForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError("Вы слишком молоды")

        return data

    def clean_avatar(self):
        data = self.cleaned_data['avatar']
        if data is True and data.image.width > 300:
            raise ValidationError("Ширина аватара не должна превышать 300 пикселей")

        return data


class ShopUserAdminUpdateForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'last_name',
                  'email', 'age', 'avatar', 'is_superuser', 'is_active')

    def __init__(self, *args, **kwargs):
        super(ShopUserAdminUpdateForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError("Вы слишком молоды")

        return data

    def clean_avatar(self):
        data = self.cleaned_data['avatar']
        if data is True and data.image.width > 300:
            raise ValidationError("Ширина аватара не должна превышать 300 пикселей")

        return data


class ProductCategoryAdminUpdateForm(ModelForm):
    class Meta:
        model = ProductCategory
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProductCategoryAdminUpdateForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class ProductAdminUpdateForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProductAdminUpdateForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
