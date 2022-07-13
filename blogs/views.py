from django.shortcuts import render
from .serializers import *
from rest_framework.generics import *
from .models import *

# Create your views here.
class PostListView(ListAPIView):
    queryset = Post.objects.all().order_by('-id')
    serializer_class = PostSerializer

class PostCreateView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostRetreiveAPIView(RetrieveAPIView):
    lookup_field = "slug"
    queryset = Post.objects.all()
    serializer_class = PostSerializer  

class PostUpdateView(RetrieveUpdateAPIView):
    lookup_field = "slug"
    queryset = Post.objects.all()
    serializer_class = PostSerializer       

class PostDestroyView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer 




class CommentListView(ListAPIView):
    queryset = Comment.objects.all().order_by('-id')
    serializer_class = CommentSerializer

class CommentCreateView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentRetreiveAPIView(RetrieveAPIView):
    lookup_field = "slug"
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer  

class CommentUpdateView(RetrieveUpdateAPIView):
    lookup_field = "slug"
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer       

class CommentDestroyView(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer       