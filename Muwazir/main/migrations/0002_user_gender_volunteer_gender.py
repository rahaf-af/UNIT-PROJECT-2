# Generated by Django 5.1.7 on 2025-04-07 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Gender',
            field=models.CharField(default='M', max_length=512),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='Gender',
            field=models.CharField(default='M', max_length=512),
        ),
    ]
