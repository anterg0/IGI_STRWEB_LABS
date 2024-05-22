# Generated by Django 5.0.6 on 2024-05-22 14:53

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+375XXXXXXXXX'.", regex='((\\+375)?(29|33|44|25)\\d{7})')])),
                ('city', models.CharField(max_length=100)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('manufacturing_status', models.CharField(choices=[('PROD_STOP', 'Снято с производства'), ('IN_PROD', 'В производстве')], max_length=20)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IGI.model')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IGI.producttype')),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_order', models.DateField()),
                ('date_of_fulfillment', models.DateField()),
                ('quantity', models.IntegerField()),
                ('client_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IGI.client')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IGI.product')),
            ],
        ),
    ]
