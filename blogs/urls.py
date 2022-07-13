from .views import *

from django.urls import path

urlpatterns = [
    path('blogs/', PostListView.as_view()),
    path('blogs/create/', PostCreateView.as_view()),
    path('blogs/<slug:slug>/', PostRetreiveAPIView.as_view()),
    path('blogs/update/<slug:slug>/', PostUpdateView.as_view()),
    path('blogs/delete/<int:id>/', PostDestroyView.as_view()),

]
