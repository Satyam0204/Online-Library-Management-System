# Generated by Django 4.0.4 on 2022-06-20 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0046_alter_book_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='datecreated',
            new_name='dateordered',
        ),
    ]
