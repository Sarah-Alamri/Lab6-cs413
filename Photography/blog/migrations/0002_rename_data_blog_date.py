# Generated by Django 4.2.1 on 2023-05-16 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='data',
            new_name='date',
        ),
    ]
