from .models import Article
from django.forms import ModelForm, TextInput, DateInput

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'full_text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи',
            }),
            'full_text': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи',
            }),
            'date': DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'дд.мм.гггг',
            })
        }