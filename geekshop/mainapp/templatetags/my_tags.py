from django import template
from django.conf import settings

register = template.Library()


@register.filter(name='media_folder_products')
def media_folder_products(string):
    if not string:
        string = 'products_image/no_img.jpg'

    return f'{settings.MEDIA_URL}{string}'


@register.filter(name='media_folder_users')
def media_folder_users(string):
    if not string:
        string = 'users_avatars/default_avatar.png'

    return f'{settings.MEDIA_URL}{string}'

# register.filter('media_folder_products', media_folder_products)
