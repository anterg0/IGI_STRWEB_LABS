from django.db import models
from django.core.validators import RegexValidator

class ProductType(models.Model):
    type_name = models.CharField(max_length=100)

    def __str__(self):
        return self.type_name

class Model(models.Model):
    model_name = models.CharField(max_length=100)
    # TODO: Add other relevant attributes for the Model

    def __str__(self):
        return self.model_name

class Product(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    MANUFACTURING_STATUS_CHOICES = [
        ('PROD_STOP', 'Снято с производства'),
        ('IN_PROD', 'В производстве'),
    ]
    manufacturing_status = models.CharField(max_length=20, choices=MANUFACTURING_STATUS_CHOICES)

    def __str__(self):
        return self.name

class Client(models.Model):
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    city = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name

class Sales(models.Model):
    date_of_order = models.DateField()
    date_of_fulfillment = models.DateField()
    client_company = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"Sale {self.id} - {self.product.name}"