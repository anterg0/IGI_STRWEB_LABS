from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
import re
from django.contrib.auth.models import AbstractUser
from datetime import date, datetime

class Article(models.Model):
    title = models.CharField('Название статьи', max_length=500)
    full_text = models.TextField('Текст статьи')
    first_sentence = models.CharField('Первое предложение', max_length=500, null=True, blank=True)
    date = models.DateField('Дата статьи')
    picture = models.ImageField(upload_to='article_photos/', blank=True, null=True)
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
    phone = models.CharField('Номер телефона', validators=[phone_regex], max_length=17, blank=True)
    city = models.CharField('Город', max_length=100)
    address = models.TextField('Адрес')
    date_of_birth = models.DateField('Дата рождения', blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    @property
    def age(self):
        if self.date_of_birth:
            today = date.today()
            age = today.year - self.date_of_birth.year
            if today.month < self.date_of_birth.month or (
                    today.month == self.date_of_birth.month and today.day < self.date_of_birth.day):
                age -= 1
            return age
        return None

    def __str__(self):
        return self.username
    
class Sales(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', default=None, blank=True)
    date_of_order = models.DateField('Дата заказа', blank=True, default=datetime.today().strftime('%Y-%m-%d'))
    date_of_fulfillment = models.DateField('Дата выполнения', blank=True, null=True)
    products = models.ManyToManyField(Product, through='SalesItem', verbose_name="Продукты")
    promo_code = models.CharField('Промокод', blank=True, null=True, max_length=50)
    total = models.FloatField('Цена заказа', default=0)

    def __str__(self):
        return f"Sale {self.id} - User {self.user.username}"
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

class SalesItem(models.Model):
    sale = models.ForeignKey(Sales, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField('Количество продукта')

    def total_price(self):
        return self.quantity * self.product.price

class Job(models.Model):
    job_name = models.CharField('Название вакансии', max_length=100)
    description = models.TextField('Описание вакансии')

    def __str__(self):
        return self.job_name
    
    def get_absolute_url(self):
        return f'/jobs/{self.id}'
    
    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

class Review(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    review_text = models.CharField('Текст отзыва', max_length=500)
    rating = models.IntegerField('Оценка', validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return self.review_text

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField('CartItem', related_name='cart_items', blank=True)

    def __str__(self):
        return f"Cart of {self.user.username}"

    def total_price(self):
        return sum(item.total_price() for item in self.cart_items.all())

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='cart_items', on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='prod')
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    def total_price(self):
        return self.quantity * self.product.price