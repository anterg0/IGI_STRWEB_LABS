from django.db import models
from django.core.validators import RegexValidator

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
    code = models.CharField('Код клиента',max_length=100)
    name = models.CharField('Наименование клиента',max_length=100)
    phone_regex = RegexValidator(regex=r'((\+375)?(29|33|44|25)\d{7})', message="Phone number must be entered in the format: '+375XXXXXXXXX'.")
    phone = models.CharField('Номер телефона',validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    city = models.CharField('Город',max_length=100)
    address = models.TextField('Адрес')

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