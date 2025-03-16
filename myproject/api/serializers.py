# myproject\api\serializers.py
from rest_framework import serializers
from .models import Book, Category

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        extra_kwargs = {
            'title': {'help_text': 'Название книги'},
            'author': {'help_text': 'Автор книги'},
            'published_date': {'help_text': 'Дата публикации (формат YYYY-MM-DD)'},
            'category': {'help_text': 'Категория книги'},
        }

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        extra_kwargs = {
            'name': {'help_text': 'Название категории'},
            'description': {'help_text': 'Описание категории (опционально)'},
        }

class CategoryDetailSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'
