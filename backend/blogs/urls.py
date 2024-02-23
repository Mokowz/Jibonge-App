from django.urls import path

from .views import (BlogListView, 
                    TagListView,
                    BlogInstanceView,
                    AuthorListView
                    )

urlpatterns = [
    path('blogs/', BlogListView.as_view(), name='blog_list'),
    path('blogs/<int:pk>/', BlogInstanceView.as_view(), name='blog_instance'),
    path('tags/', TagListView.as_view(), name='tag_list'),
    path('authors/', AuthorListView.as_view(), name='author_list'),
]