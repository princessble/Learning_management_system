# Generated by Django 5.1.1 on 2024-12-20 13:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_classes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
