# Generated by Django 5.1.7 on 2025-04-12 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='rating',
            field=models.IntegerField(blank=True, choices=[(1, '⭐'), (2, '⭐⭐'), (3, '⭐⭐⭐'), (4, '⭐⭐⭐⭐'), (5, '⭐⭐⭐⭐⭐')], null=True),
        ),
    ]
