from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from django.db import transaction
from django.contrib.auth.decorators import login_required

from authapp.forms import ShopUserProfileUpdateForm
from authapp.models import ShopUser
from authapp.forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserUpdateForm


def login(request):
    next = request.GET['next'] if 'next' in request.GET.keys() else None

    if request.method == 'POST':
        form = ShopUserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username,
                                     password=password)
            if user and user.is_active:
                next = request.POST['next'] if 'next' in request.POST.keys() else None
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index') if not next else next)
    else:
        form = ShopUserLoginForm()

    context = {
        'title': 'регистрация',
        'form': form,
        'next': next,
    }

    return render(request, 'authapp/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:index'))


def register(request):
    if request.method == 'POST':
        form = ShopUserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            if send_verify_mail(user):
                print('сообщение подтверждения отправлено')
                return HttpResponseRedirect(reverse('auth:login'))
            else:
                print('ошибка отправки сообщения')
                return HttpResponseRedirect(reverse('auth:login'))
    else:
        form = ShopUserRegisterForm()

    context = {
        'page_title': 'регистрация в системе',
        'form': form,
    }

    return render(request, 'authapp/register.html', context)


def send_verify_mail(user):
    verify_link = reverse('auth:verify',
                          args=[user.email, user.activation_key])

    page_title = f'Подтверждение учётной записи {user.username}'
    message = f'Для подтверждения учётной записи {user.username} на портале {settings.DOMAIN_NAME} перейдите ' \
              f'по ссылке: \n{settings.DOMAIN_NAME}{verify_link}'

    return send_mail(page_title, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)


def verify(request, email, activation_key):
    try:
        user = ShopUser.objects.get(email=email)
        if user.activation_key == activation_key and not user.is_activation_key_expires():
            print(user.activation_key, activation_key)
            user.is_active = True
            user.save()
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')

            return render(request, 'authapp/verification.html')
        else:
            print(f'error activation user {user}')
            return render(request, 'authapp/verification.html')
    except Exception as e:
        print(f'except error activation user: {e.args}')
        return HttpResponseRedirect(reverse('main:index'))


@login_required
@transaction.atomic
def update(request):

    if request.method == 'POST':
        form = ShopUserUpdateForm(request.POST, request.FILES,
                                     instance=request.user)
        profile_form = ShopUserProfileUpdateForm(request.POST,
                                               instance=request.user.shopuserprofile)
        if form.is_valid() and profile_form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('auth:update'))
    else:
        form = ShopUserUpdateForm(instance=request.user)
        profile_form = ShopUserProfileUpdateForm(instance=request.user.shopuserprofile)

    context = {
        'page_title': 'редактирование',
        'form': form,
        'profile_form': profile_form,
    }

    return render(request, 'authapp/update.html', context)
