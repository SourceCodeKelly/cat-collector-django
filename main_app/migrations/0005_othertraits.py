# Generated by Django 4.0.5 on 2022-06-02 01:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_cat_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtherTraits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('other_trait', models.CharField(max_length=20)),
                ('trait_info', models.TextField(max_length=500)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='other_traits', to='main_app.cat')),
            ],
        ),
    ]