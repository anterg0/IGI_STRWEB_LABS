from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.decorators import method_decorator
from .models import FAQModel, Article, PromoCode, Job, Product, User, Review, Sales, Cart, CartItem, SalesItem
from .forms import ArticleForm, CustomUserCreationForm, JobForm, ProductForm, SaleForm, ReviewForm, UserProfilePictureForm
import requests
from .decorators import is_employee_or_superuser, is_auth
from datetime import timedelta
from django.utils import timezone
from django.db.models import Q
from datetime import datetime
import pandas as pd
import plotly.express as px

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
        form = ArticleForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/news')
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
    user_timezone = request.session.get('django_timezone')
    if user_timezone:
        timezone.activate(user_timezone)
    orders = request.user.sales_set.all()
    sales_items = SalesItem.objects.all()
    data = {
        'orders': orders,
        'sales_items': sales_items
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
def cart_add(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
    
        if not product_id:
            return redirect('goods')

        product = get_object_or_404(Product, id=product_id)
        
        cart, created = Cart.objects.get_or_create(user=request.user)

        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_item.quantity += 1
        else:
            cart_item.quantity = 1
        
        cart_item.save()
        return redirect('cart-detail')
    return redirect('goods')

def reviews_view(request):
    reviews = Review.objects.all()
    data = {
        'reviews': reviews
    }
    return render(request, 'reviews.html', data)

@login_required
def review_create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            try:
                review = form.save(commit=False)
                review.user = request.user
                review.save()
                return redirect('profile')
            except:
                return redirect('home')
    else:
        form = ReviewForm(initial={'user': request.user})
    data = {
        'form': form
    }
    return render(request, 'review_create.html', data)

class ReviewDetailView(DetailView):
    model = Review
    template_name = 'detail_view.html'
    context_object_name = 'review'


class ReviewDeleteView(DeleteView):
    model = Review
    template_name = 'delete_element.html'
    success_url = '/reviews'

class ReviewUpdateView(UpdateView):
    model = Review
    template_name = 'review_create.html'
    form_class = ReviewForm

@is_employee_or_superuser
def sales(request):
    ten_days_ago = timezone.now() - timedelta(days=10)

    fulfilled_orders = Sales.objects.filter(date_of_order__gte=ten_days_ago, date_of_fulfillment__isnull=False)
    
    all_orders = Sales.objects.all()

    sales_data = []
    dates = []
    for order in fulfilled_orders:
        order_date = order.date_of_order
        if order_date in dates:
            index = dates.index(order_date)
            sales_data[index] += order.total
        else:
            dates.append(order_date)
            sales_data.append(order.total)
    
    dates.sort()
    sales_data = [sales_data[dates.index(date)] for date in dates]
    
    df = pd.DataFrame({'Date': dates[-10:], 'Sales': sales_data[-10:]})
    fig = px.bar(df, x='Date', y='Sales', title='Общий объем продаж за 10 дней (только выполненные заказы)')
    fig.update_layout(xaxis_title='Дата', yaxis_title='Прибыль')
    chart = fig.to_html(full_html=False)

    sales_items = SalesItem.objects.all()

    data = {
        'fulfilled_orders': fulfilled_orders,
        'all_orders': all_orders,
        'chart': chart,
        'sales_items': sales_items
    }
    return render(request, 'sales.html', data)


def contacts_view(request):
    contacts = User.objects.filter(Q(is_employee=True) | Q(is_superuser=True))
    data = {
        'contacts': contacts
    }
    return render(request, 'contacts.html', data)

def fulfill(request, pk):
    order = get_object_or_404(Sales, id=pk)
    if request.method == 'POST':
        order.date_of_fulfillment = timezone.now()
        order.save()
    return redirect('/sales')    

@login_required
def update_profile_picture(request):
    if request.method == 'POST':
        form = UserProfilePictureForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfilePictureForm(instance=request.user)
    return render(request, 'update_picture.html', {'form': form})

@login_required
def cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    return render(request, 'cart.html', {'cart': cart})

@login_required
def checkout(request):
    if request.method == 'POST':
        cart = Cart.objects.get(user=request.user)
        post_data = request.POST
        print("POST data: ", post_data)

        quantities = {key.split('[')[1][:-1]: value for key, value in post_data.items() if key.startswith('quantities[')}
        print(f"Quantities from form: {quantities}")

        promo_code = post_data.get('promo_code', '').strip()

        sale = Sales(
            user=request.user,
            date_of_order=datetime.today().strftime('%Y-%m-%d'),
            promo_code=promo_code
        )
        sale.save()

        total_amount = 0

        if quantities:
            for item_id, quantity in quantities.items():
                quantity = int(quantity)
                if quantity > 0:
                    cart_item = CartItem.objects.get(id=item_id, cart=cart)
                    cart_item.quantity = quantity
                    cart_item.save()

                    SalesItem.objects.create(
                        sale=sale,
                        product=cart_item.product,
                        quantity=quantity
                    )
                    total_amount += cart_item.product.price * quantity

            if promo_code:
                try:
                    promo_dis = PromoCode.objects.get(name=promo_code).discount
                    total_amount *= (1 - promo_dis)
                except PromoCode.DoesNotExist:
                    print("Invalid promo code")

            sale.total = total_amount
            sale.save()

            cart.cart_items.all().delete()
            
            return redirect('profile')

    return redirect('cart-detail')

def html_examples(request):
    return render(request, 'html_examples.html')

@login_required
def delete_cart_item(request, pk):
    cart_item = get_object_or_404(CartItem, id=pk)
    if cart_item:
        cart_item.delete()
    return redirect('cart-detail')