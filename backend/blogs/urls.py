from django.urls import path

from .views import (BlogListView, 
                    TagListView,
                    )

urlpatterns = [
    path('blogs/', BlogListView.as_view(), name='blog_list'),
    path('tags/', TagListView.as_view(), name='tag_list'),
]