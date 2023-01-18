from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .forms import *
from .models import *
from .utils import *


def about_us(request):
    return render(request,'pixel/about.html', {'title':'Вдохновители', 'menu': menu})


def show_best(request,name_id):
    games = Game.objects.all()
    janr_filter = set()
    name_id = str(name_id)
    bests = get_object_or_404(Best, name=name_id)
    filter = Game.objects.filter(best_id=bests.pk)
    for i in filter:
        janr_filter.add(i.janr_id)
    janrs = Janr.objects.filter(pk__in=janr_filter)

    return render(request, 'pixel/show_best.html', {'title': 'Лучшее за ' + name_id, 'menu': menu, 'games': games,
                                                    'janrs': janrs,'bests': bests, 'name_id': name_id})

def show_janr(request, name_id): # нет класса представления, так как url_kwarg работает только для pk и slug
    janrs = get_object_or_404(Janr, name=name_id)
    games = Game.objects.filter(janr_id=janrs.pk)
    return render(request, 'pixel/show_janr.html', {'title': 'Лучшие ' + janrs.name, 'menu': menu, 'games': games,
                                                    'janrs': janrs, 'name_id': name_id})


class PixelHome(DataMixin, ListView):
    model = Game
    context_object_name = 'games'
    template_name = 'pixel/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_content(title='Пиксель')
        context['janrs'] = Janr.objects.all()
        return context | c_def


class Bests(DataMixin, ListView):
    model = Best
    context_object_name = 'bests'
    template_name = 'pixel/best.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_content(title = 'Подборка лучших игр по годам')
        return context | c_def


class Categorie(DataMixin, ListView):
    model = Janr
    context_object_name = 'janrs'
    template_name = 'pixel/categorie.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_content(title = 'Жанры')
        return context | c_def


class Addgame(DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'pixel/addgame.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_content(title = 'Добавление игры')
        return context | c_def


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'pixel/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_content(title="Регистрация")
        return context | c_def

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'pixel/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_content(title="Авторизация")
        return context | c_def

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')
