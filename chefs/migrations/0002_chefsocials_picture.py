# Generated by Django 4.0.2 on 2022-04-12 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chefs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chefsocials',
            name='picture',
            field=models.ImageField(null=True, upload_to='chefs/', verbose_name='Chef profile photo'),
        ),
    ]