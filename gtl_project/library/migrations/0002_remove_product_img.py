# Generated by Django 4.2.2 on 2024-02-26 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='img',
        ),
    ]