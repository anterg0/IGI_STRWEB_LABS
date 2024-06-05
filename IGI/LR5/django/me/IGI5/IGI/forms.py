from .models import Article, User, Job, Product, Sales, Review
from django.forms import ModelForm, TextInput, DateInput, Textarea, NumberInput
from django.contrib.auth.forms import UserCreationForm
from django import forms

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'full_text', 'date', 'picture']

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

class SaleForm(ModelForm):
    class Meta:
        model = Sales
        fields = ['quantity', 'product', 'user', 'date_of_order', 'promo_code']

class ReviewForm(ModelForm):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]

    rating = forms.ChoiceField(
        label='Rating',
        choices=RATING_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )
    class Meta:
        model = Review
        fields = ('review_text', 'rating')
        widgets = {
            'review_text': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Текст отзыва',
            }),
        }

class UserProfilePictureForm(ModelForm):
    class Meta:
        model = User
        fields = ['profile_picture']