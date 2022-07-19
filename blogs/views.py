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
    serializer_class = PostCreateSerializer

class PostRetreiveAPIView(RetrieveAPIView):
    lookup_field = "slug"
    queryset = Post.objects.all()
    serializer_class = PostSerializer  

class PostUpdateView(RetrieveUpdateAPIView):
    lookup_field = "slug"
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer       

class PostDestroyView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer 




class ReplyListView(ListAPIView):
    queryset = Reply.objects.all().order_by('-id')
    serializer_class = ReplySerializer

class ReplyCreateView(CreateAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer

class ReplyRetreiveAPIView(RetrieveAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer  

class ReplyUpdateView(RetrieveUpdateAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer       

class ReplyDestroyView(DestroyAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
    

class CommentListView(ListAPIView):
    queryset = Comment.objects.all().order_by('-id')
    serializer_class = CommentSerializer

class CommentCreateView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentRetreiveAPIView(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer  

class CommentUpdateView(RetrieveUpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer   
    lookup_field = 'id'  

class CommentDestroyView(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer       