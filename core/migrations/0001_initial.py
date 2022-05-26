# Generated by Django 3.2.13 on 2022-05-26 19:27

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('email', models.EmailField(max_length=254)),
                ('postal_code', models.CharField(max_length=200)),
                ('zip_code', models.CharField(max_length=200)),
                ('town', models.CharField(max_length=200)),
                ('country', django_countries.fields.CountryField(max_length=2)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('id_number', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('postal_code', models.CharField(max_length=200)),
                ('zip_code', models.CharField(max_length=200)),
                ('town', models.CharField(max_length=200)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('date_employed', models.DateField(auto_now=True)),
                ('contract_end_date', models.DateField(null=True)),
                ('salary', models.FloatField(default=0)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.department')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NoticeBoard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('date_due', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WorkAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('check_in_time', models.DateTimeField(null=True)),
                ('check_out_time', models.DateTimeField(null=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.employee')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('stage', models.CharField(choices=[('todo', 'Todo'), ('in_progress', 'In Progress'), ('review', 'Review'), ('done', 'Done')], max_length=200)),
                ('date_due', models.DateTimeField()),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignees', to='core.employee')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_creators', to='core.employee')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]