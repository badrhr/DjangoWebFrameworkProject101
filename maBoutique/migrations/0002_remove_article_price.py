# Generated by Django 5.0.2 on 2024-02-26 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maBoutique', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='price',
        ),
    ]