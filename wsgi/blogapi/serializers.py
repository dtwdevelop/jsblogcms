from blog.models import Category , Page, Comment
from rest_framework import serializers

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'title','page_id','topic','category_id','pub_date',)


class PagesSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Page
        fields = ('id', 'title','topic','category_id','comments','pub_date','img_url',)


class CategorySerializer(serializers.ModelSerializer):
    pages = PagesSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        # resource_name = 'categories'

        fields = ('id', 'title_category', 'post','pages','url','hide', 'pub_date',)

