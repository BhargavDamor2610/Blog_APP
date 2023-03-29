from django.db.models import fields
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Post
        fields= ('title', 'content', 'author')