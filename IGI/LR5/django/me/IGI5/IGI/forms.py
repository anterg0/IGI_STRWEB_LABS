from .models import Article, User, Job, Product
from django.forms import ModelForm, TextInput, DateInput, Textarea, NumberInput
from django.contrib.auth.forms import UserCreationForm

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'full_text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи',
            }),
            'full_text': Textarea(attrs={
                'class': 'full_text',
                'placeholder': 'Текст статьи',
            }),
            'date': DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'дд.мм.гггг',
            })
        }

class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = ['job_name', 'description']
        widgets = {
            'job_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название вакансии',
            }),
            'description': Textarea(attrs={
                'class': 'full_text',
                'placeholder': 'Описание вакансии',
            })
        }

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'code', 'type', 'manufacturing_status', 'model']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название товара',
            }),
            'price': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена',
            }),
            'code': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Код товара',
            }),
            # 'type': ChoiceField(attrs={
            #     'class': 'form-control',
            #     'placeholder': 'Тип мебели',
            # }),
            # 'manufacturing_status': ChoiceField(attrs={
            #     'class': 'form-control',
            # }),
            'model': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Модель',
            })
        }


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone', 'city', 'address', 'date_of_birth')
        # widgets = {
        #     'username': TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Никнейм',
        #     }),
        #     'email': TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Эл. почта',
        #     }),
        #     'phone': TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Номер телефона',
        #     }),
        #     'city': TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Город',
        #     }),
        #     'address': Textarea(attrs={
        #         'class': 'full_text',
        #         'placeholder': 'Адрес',
        #     }),
        #     'date_of_birth': TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Дата рождения',
        #     }),
        # }