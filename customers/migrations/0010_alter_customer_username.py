# Generated by Django 4.1.7 on 2023-03-05 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0009_alter_customer_options_alter_customer_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='username',
            field=models.CharField(default='', max_length=200, unique=True),
        ),
    ]
