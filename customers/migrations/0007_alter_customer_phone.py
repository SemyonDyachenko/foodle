# Generated by Django 4.1.7 on 2023-03-05 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0006_alter_customer_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.TextField(max_length=12, unique=True),
        ),
    ]
