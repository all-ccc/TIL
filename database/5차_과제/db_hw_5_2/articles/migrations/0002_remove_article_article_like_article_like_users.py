# Generated by Django 4.2.11 on 2024-04-08 02:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='article_like',
        ),
        migrations.AddField(
            model_name='article',
            name='like_users',
            field=models.ManyToManyField(related_name='articles', to=settings.AUTH_USER_MODEL),
        ),
    ]
