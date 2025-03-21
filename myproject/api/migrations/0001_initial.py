# Generated by Django 5.1.3 on 2024-11-17 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название книги')),
                ('author', models.CharField(max_length=255, verbose_name='Автор')),
                ('published_date', models.DateField(verbose_name='Дата публикации')),
                ('isbn', models.CharField(max_length=13, unique=True, verbose_name='ISBN')),
                ('page_count', models.PositiveIntegerField(verbose_name='Количество страниц')),
                ('cover', models.URLField(blank=True, verbose_name='Обложка книги (URL)')),
            ],
        ),
    ]
