# Generated by Django 4.1.7 on 2023-03-05 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0004_customer_activated_alter_customer_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.IntegerField(max_length=11, unique=True),
        ),
    ]
