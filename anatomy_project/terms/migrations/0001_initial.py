# Generated by Django 5.1.7 on 2025-03-30 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('russian', models.CharField(max_length=100, verbose_name='Русский термин')),
                ('latin', models.CharField(max_length=100, verbose_name='Латинский термин')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
            ],
        ),
    ]
