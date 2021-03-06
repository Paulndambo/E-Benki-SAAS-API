# Generated by Django 3.2.13 on 2022-05-27 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0003_alter_branch_code'),
        ('customers', '0002_auto_20220526_2146'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('account_number', models.CharField(max_length=200, unique=True)),
                ('account_type', models.CharField(choices=[('savings', 'Savings Account'), ('checkig', 'Checking Account')], max_length=200)),
                ('balance', models.FloatField(default=0)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.branch')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='customers.customer')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('type', models.CharField(choices=[('deposit', 'Deposit'), ('withdraw', 'Withdraw')], max_length=200)),
                ('amount', models.FloatField(default=0)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='banking.account')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
