# Generated by Django 4.2.6 on 2023-10-14 12:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_customuser_nickname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(help_text='Required field. No more than 150 characters. Only letters, numbers and symbols @/./+/-/_.', max_length=150, unique=True, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
    ]
