# Generated by Django 4.0.4 on 2022-06-24 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0053_query'),
    ]

    operations = [
        migrations.CreateModel(
            name='customerQuery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emailid', models.EmailField(blank=True, max_length=200, null=True)),
                ('query', models.TextField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Query',
        ),
    ]
