# Generated by Django 4.0.4 on 2022-06-22 16:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0050_book_upvote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='upvote',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
