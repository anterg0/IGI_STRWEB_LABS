from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import FAQModel, Article, PromoCode, Job, Product, User
from .forms import ArticleForm, CustomUserCreationForm, JobForm, ProductForm, SaleForm
import requests
from .decorators import is_employee_or_superuser, is_auth

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

@is_employee_or_superuser
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
    if request.user.is_authenticated:
        return redirect('home')
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

@method_decorator(is_employee_or_superuser, name='dispatch')
class NewsUpdateView(UpdateView):
    model = Article
    template_name = 'create_article.html'
    form_class = ArticleForm

@method_decorator(is_employee_or_superuser, name='dispatch')
class NewsDeleteView(DeleteView):
    model = Article
    template_name = 'delete_element.html'
    success_url = '/news'

def api_view(request):
    return render(request, 'api.html')

@login_required
def profile(request):
    orders = request.user.sales_set.all()
    for el in orders:
        el.total = el.quantity * el.product.price
        if el.promo_code:
            promo_dis = PromoCode.objects.filter(name=el.promo_code)[0].discount
            el.total *= promo_dis
    data = {
        'orders': orders
    }
    return render(request, 'profile.html', data)

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

def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    data = {
        'form': form
    }
    return render(request, 'register.html', data)

def jobs(request):
    jobs = Job.objects.all()
    data = {
        'jobs': jobs
    }
    return render(request, 'jobs.html', data)

@is_employee_or_superuser
def create_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jobs')
    else:
        form = JobForm()
    return render(request, 'jobs_create.html', {'form': form})


class JobDetailView(DetailView):
    model = Job
    template_name = 'detail_view.html'
    context_object_name = 'job'

@method_decorator(is_employee_or_superuser, name='dispatch')
class JobDeleteView(DeleteView):
    model = Job
    template_name = 'delete_element.html'
    success_url = '/jobs'

@method_decorator(is_employee_or_superuser, name='dispatch')
class JobUpdateView(UpdateView):
    model = Job
    template_name = 'jobs_create.html'
    form_class = JobForm

def goods(request):
    goods = Product.objects.all()
    sort_order = request.GET.get('sort_order', 'asc')
    if sort_order == 'asc':
        goods = Product.objects.order_by('price')
    else:
        goods = Product.objects.order_by('-price')
    return render(request, 'goods.html', {'goods': goods})

def create_goods(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('goods')
    else:
        form = ProductForm()
    return render(request, 'goods_create.html', {'form': form})

@is_employee_or_superuser
def all_customers(request):
    customers = User.objects.order_by('city').filter(is_employee=False, is_superuser=False)
    data = {
        'customers': customers
    }
    return render(request, 'customers.html', data)

@login_required
def order_create_view(request):
    item_id = request.GET.get('item_id')
    if not item_id:
        return redirect('goods')
    item = get_object_or_404(Product, id=item_id)
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            sale = form.save(commit=False)
            sale.product = item
            sale.user = request.user
            sale.save()
            return redirect('profile')
    else:
        form = SaleForm(initial={'product': item, 'user': request.user})
    return render(request, 'order_create.html', {'item': item, 'form': form})