# Generated by Django 4.0.2 on 2022-04-12 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chefs', '0003_remove_chefsocials_picture_chef_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='chef',
            name='working',
            field=models.BooleanField(default=True, verbose_name='Is chef working?'),
        ),
    ]
