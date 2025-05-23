# Generated by Django 5.1.7 on 2025-04-12 17:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_profile_photo_user_profile_photo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('location', models.CharField(max_length=200)),
                ('notes', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='pending', max_length=20)),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='main.user')),
                ('volunteer_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='main.volunteer')),
            ],
        ),
    ]
