# Generated by Django 4.2 on 2023-08-17 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='title',
            field=models.CharField(default='', max_length=150),
        ),
    ]
