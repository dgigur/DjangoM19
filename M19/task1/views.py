from django.shortcuts import render
from .forms import UserRegister
from .models import *


# Create your views here.
def platform(request):
    title = 'Главная страница'
    context = {
        'title': title,
    }
    return render(request, 'platform.html', context)


def games(request):
    title = 'Игры'
    list_of_games = Game.objects.all()
    context = {
        'list_of_games': list_of_games,
        'title': title
    }
    return render(request, 'games.html', context)


def cart(request):
    title = 'Корзина'
    context = {
        'title': title,
    }
    return render(request, 'cart.html', context)


def sign_up_by_django(request):
    hello = ''
    error = ''
    if request.method == "POST":
        form = UserRegister(request.POST)
        users = Buyer.objects.all()
        info = {}
        context = {
            'users': users,
            'info': info,
            'form': form,
            }
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            for user in users:
                if username == user.name:
                    error = 'Пользователь уже существует'
                    break
            if password != repeat_password:
                error = 'Пароли не совпадают'
            #if int(age) < 18:
            #    error = 'Вы должны быть старше 18'
            if error == '':
                Buyer.objects.create(name=username, age=age)
                hello = f"Приветствуем, {username}!"
            context.update({"username": username,
                            "password": password,
                            "repeat_password": repeat_password,
                            'age': age,
                            'error': error,
                            'hello': hello,
                            })
            return render(request, 'registration_page.html', context)
    form = UserRegister()
    return render(request, 'registration_page.html', {'form': form})
