# Generated by Django 5.1 on 2024-09-04 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='realisateur',
            name='date_naissance',
        ),
    ]
