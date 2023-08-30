from rest_framework import serializers
from .models import Categories, Post

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        #fields = ('id', 'title', 'description')
        fields = '__all__'

class PostContentSerializer(serializers.ModelSerializer):

    category = CategorySerializer()
    class Meta:
        model = Post
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'