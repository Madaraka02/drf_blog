from .views import *

from django.urls import path

urlpatterns = [
    path('blogs/', PostListView.as_view()),
    path('blogs/create/', PostCreateView.as_view()),
    path('blogs/<slug:slug>/', PostRetreiveAPIView.as_view()),
    path('blogs/update/<slug:slug>/', PostUpdateView.as_view()),
    path('blogs/delete/<int:id>/', PostDestroyView.as_view()),


    path('comments/', CommentListView.as_view()),
    path('comments/create/', CommentCreateView.as_view()),
    path('comments/<int:id>/', CommentRetreiveAPIView.as_view()),
    path('comments/update/<int:id>/', CommentUpdateView.as_view()),
    path('comments/delete/<int:id>/', CommentDestroyView.as_view()),

    path('replies/', ReplyListView.as_view()),
    path('replies/create/', ReplyCreateView.as_view()),
    path('replies/<int:id>/', ReplyRetreiveAPIView.as_view()),
    path('replies/update/<int:id>/', ReplyUpdateView.as_view()),
    path('replies/delete/<int:id>/', ReplyDestroyView.as_view()),

]
