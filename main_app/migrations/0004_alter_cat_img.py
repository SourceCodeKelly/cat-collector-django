# Generated by Django 4.0.5 on 2022-06-01 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_remove_cat_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='img',
            field=models.CharField(max_length=500),
        ),
    ]