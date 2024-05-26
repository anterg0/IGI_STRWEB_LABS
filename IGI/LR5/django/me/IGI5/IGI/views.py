from django.shortcuts import render
from django.views.generic import DetailView
from .models import FAQModel, Article
from .forms import ArticleForm

# Create your views here.
def home(request):
    return render(request, 'home.html')
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