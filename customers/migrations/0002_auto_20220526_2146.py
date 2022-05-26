# Generated by Django 3.2.13 on 2022-05-26 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_branch_code'),
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.branch'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='scanned_id',
            field=models.ImageField(upload_to='scanned_ids'),
        ),
    ]