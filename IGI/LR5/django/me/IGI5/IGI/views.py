from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import FAQModel, Article, PromoCode
from .forms import ArticleForm
import requests

# Create your views here.
def home(request):
    news = Article.objects.order_by('-date').first()
    data = {
        'news': news
    }
    return render(request, 'home.html', data)

def about(request):
    return render(request, 'about.html')

def faq(request):
    data = {
        'faqs': FAQModel.objects.all()
    }
    return render(request, 'faq.html', data)

def coc(request):
    return render(request, 'codeofcond.html')

def news(request):
    data = {
        'news': Article.objects.order_by('-date')
    }
    return render(request, 'news.html', data)

class NewsDetailView(DetailView):
    model = Article
    template_name = 'detail_view.html'
    context_object_name = 'article'

def create_article(request):
    error = ''
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Данные заполнены неверно'
    form = ArticleForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'create_article.html', data)

def login_view(request):
    error = ''
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            try:
                form.clean()
                login(request, form.get_user())
                return redirect('home')
            except:
                error = 'Некорректные данные'
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form, 'error': error})

def logout_view(request):
    logout(request)
    return redirect('home')

class NewsUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    template_name = 'create_article.html'
    form_class = ArticleForm

class NewsDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'news_delete.html'
    success_url = '/news'

def api_view(request):
    return render(request, 'api.html')

@login_required
def profile(request):
    return render(request, 'profile.html')

def promo_view(request):
    promos = PromoCode.objects.all()
    data = {
        'promocodes': promos
    }
    for el in data['promocodes']:
        el.discount *= 100
    return render(request, 'promo.html', data)

def api_view(request):
    fact = {
        'fact': "Couldn't get the cat fact"
    }
    joke = {
        'setup': 'No',
        'punchline': 'jokes for you'
    }
    response = ''
    try:
        response = requests.get('https://catfact.ninja/fact')
        if response.status_code == 200:
            fact = response.json()
    except:
        pass
    try:
        response = requests.get('https://official-joke-api.appspot.com/random_joke')
        if response.status_code == 200:
            joke = response.json()
    except:
        pass

    data = {
        'fact': fact,
        'joke': joke
    }
    return render(request, 'api.html', data)