from django.urls import path

from .views import (BlogListView, 
                    TagListView,
                    BlogInstanceView,
                    )

urlpatterns = [
    path('blogs/', BlogListView.as_view(), name='blog_list'),
    path('blogs/<int:pk>/', BlogInstanceView.as_view(), name='blog_instance'),
    path('tags/', TagListView.as_view(), name='tag_list'),
]