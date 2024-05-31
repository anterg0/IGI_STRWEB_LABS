from django.db import models
from django.core.validators import RegexValidator
import re
from django.contrib.auth.models import AbstractUser
from datetime import date

class Article(models.Model):
    title = models.CharField('Название статьи', max_length=500)
    full_text = models.TextField('Текст статьи')
    first_sentence = models.CharField('Первое предложение', max_length=500, null=True, blank=True)
    date = models.DateField('Дата статьи')
    def __str__(self):
        return self.title
    def save(self, update_fields=None, *args, **kwargs):
        if update_fields is None or 'full_text' in update_fields:
            first_sentence = re.split(r'(?<=[.!?])\s+', self.full_text.strip())[0]
            self.first_sentence = first_sentence[:500]
        super(Article, self).save(update_fields=update_fields, *args, **kwargs)

    def get_absolute_url(self):
        return f'/news/{self.id}'
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class Product(models.Model):
    name = models.CharField('Наименование мебели',max_length=100)
    code = models.CharField('Код мебели',max_length=100)
    model = models.CharField('Название модели', max_length=50)
    price = models.DecimalField('Цена',max_digits=10, decimal_places=2)
    MANUFACTURING_STATUS_CHOICES = [
        ('PROD_STOP', 'Снято с производства'),
        ('IN_PROD', 'В производстве'),
    ]
    PRODUCT_TYPES = {
        'kitchen': 'Кухонная',
        'office': 'Офисная',
        'cabinet': 'Кабинетная'
    }
    manufacturing_status = models.CharField('Состояние производства',max_length=20, choices=MANUFACTURING_STATUS_CHOICES)
    type = models.CharField('Вид мебели', max_length=40, choices=PRODUCT_TYPES)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

class Client(models.Model):
    # code = models.CharField('Код клиента',max_length=100)
    name = models.CharField('Наименование клиента',max_length=100)
    phone_regex = RegexValidator(regex=r'((\+375)?(29|33|44|25)\d{7})', message="Номер телефона должен быть в формате: '+375XXXXXXXXX'.")
    phone = models.CharField('Номер телефона',validators=[phone_regex], max_length=17, blank=True)
    city = models.CharField('Город',max_length=100)
    address = models.TextField('Адрес')
    is_employee = models.BooleanField('Является ли сотрудником', default=False)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

class Sales(models.Model):
    date_of_order = models.DateField('Дата заказа')
    date_of_fulfillment = models.DateField('Дата выполнения')
    client_company = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент заказчик')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Наименование продукта')
    quantity = models.IntegerField('Количество продукта')

    def __str__(self):
        return f"Sale {self.id} - {self.product.name}"
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

class PromoCode(models.Model):
    name = models.CharField('Название промокода', max_length=30)
    discount_validator = RegexValidator(regex=r'^1|0\.\d{2}$', message="Скидка должна быть введена в формате: 1 или 0.XX")
    discount = models.DecimalField('Скидка', validators=[discount_validator], max_digits=4, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Промокод'
        verbose_name_plural = 'Промокоды'
class FAQModel(models.Model):
    question = models.TextField('Вопрос')
    answer = models.TextField('Ответ на вопрос')
    def __str__(self):
        return self.question
    class Meta:
        verbose_name = 'Вопрос-ответ'
        verbose_name_plural = 'Вопросы-ответы'

class User(AbstractUser):
    is_employee = models.BooleanField('Сотрудник?', default=False)
    phone_regex = RegexValidator(regex=r'((\+375)?(29|33|44|25)\d{7})', message="Номер телефона должен быть в формате: '+375XXXXXXXXX'.")
    phone = models.CharField('Номер телефона',validators=[phone_regex], max_length=17, blank=True)
    city = models.CharField('Город',max_length=100)
    address = models.TextField('Адрес')
    date_of_birth = models.DateField('Дата рождения', blank=True, null=True)
    @property
    def age(self):
        if self.date_of_birth:
            today = date.today ()
            age = today.year - self.date_of_birth.year
            if today.month < self.date_of_birth.month or (
                    today.month == self.date_of_birth.month and today.day < self.date_of_birth.day):
                age -= 1
            return age
        return None

    def __str__(self):
        return self.username

class Job(models.Model):
    job_name = models.CharField('Название вакансии', max_length=100)
    description = models.TextField('Описание вакансии')

    def __str__(self):
        return self.job_name
    
    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'