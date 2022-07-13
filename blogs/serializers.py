from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'        

class PostSerializer(ModelSerializer):
    comments = CommentSerializer(many=True)
    # comments = serializers.HyperlinkedRelatedField(many=True,read_only=True, view_name='')
    # serializers.StringRelatedField(many=True)
    # serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # serializers.HyperlinkedRelatedField(many=True,read_only=True)
    class Meta:
        model = Post
        fields = ['id','title','slug','image','description','comments','snippet','created_at', 'updated_at']
