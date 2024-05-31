from django.db import models
from django.core.validators import RegexValidator
import re

class Article(models.Model):
    title = models.CharField('Название статьи', max_length=500)
    full_text = models.TextField('Текст статьи')
    first_sentence = models.CharField('Первое предложение', max_length=500, null=True, blank=True)
    date = models.DateField('Дата статьи')
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        if not self.first_sentence:
            first_sentence = re.split(r'(?<=[.!?])\s+', self.full_text.strip())[0]
            self.first_sentence = first_sentence[:500]
        super(Article, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return f'/news/{self.id}'
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class ProductType(models.Model):
    type_name = models.CharField('Название вида',max_length=100)

    def __str__(self):
        return self.type_name
    class Meta:
        verbose_name = 'Вид продукта'
        verbose_name_plural = 'Виды продуктов'

class Model(models.Model):
    model_name = models.CharField('Название модели',max_length=50)

    def __str__(self):
        return self.model_name
    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'

class Product(models.Model):
    name = models.CharField('Наименование продукта',max_length=100)
    code = models.CharField('Код продукта',max_length=100)
    type = models.ForeignKey(ProductType, on_delete=models.CASCADE, verbose_name='Вид продукта')
    model = models.ForeignKey(Model, on_delete=models.CASCADE, verbose_name='Модель')
    price = models.DecimalField('Цена продукта',max_digits=10, decimal_places=2)
    MANUFACTURING_STATUS_CHOICES = [
        ('PROD_STOP', 'Снято с производства'),
        ('IN_PROD', 'В производстве'),
    ]
    manufacturing_status = models.CharField('Состояние производства',max_length=20, choices=MANUFACTURING_STATUS_CHOICES)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

class Client(models.Model):
    # code = models.CharField('Код клиента',max_length=100)
    name = models.CharField('Наименование клиента',max_length=100)
    phone_regex = RegexValidator(regex=r'((\+375)?(29|33|44|25)\d{7})', message="Номер телефона должен быть в формате: '+375XXXXXXXXX'.")
    phone = models.CharField('Номер телефона',validators=[phone_regex], max_length=17, blank=True) # validators should be a list
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