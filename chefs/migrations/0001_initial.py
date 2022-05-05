# Generated by Django 4.0.2 on 2022-04-12 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=150, verbose_name='chef position')),
            ],
            options={
                'verbose_name': 'chef',
                'verbose_name_plural': 'chefs',
            },
        ),
        migrations.CreateModel(
            name='ChefSocials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_name', models.CharField(max_length=100, verbose_name='Social account name')),
                ('link', models.URLField(verbose_name='user link')),
                ('chef', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chefs.chef')),
            ],
            options={
                'verbose_name': 'Chef social',
                'verbose_name_plural': 'Chef socials',
            },
        ),
    ]
