# Generated by Django 4.0.2 on 2022-04-12 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_alter_menuitems_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitems',
            name='active',
            field=models.BooleanField(default=True, verbose_name='activate item'),
        ),
    ]
