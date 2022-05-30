# Generated by Django 3.2.13 on 2022-05-30 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_type',
            field=models.CharField(choices=[('savings', 'Savings Account'), ('checking', 'Checking Account')], max_length=200),
        ),
    ]
