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