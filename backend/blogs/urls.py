from django.urls import path

from .views import (BlogListView, 
                    TagListView,
                    BlogInstanceView,
                    AuthorListView,
                    BlogSearchView,
                    BlogFilterView
                    )

urlpatterns = [
    path('blogs/', BlogListView.as_view(), name='blog_list'),
    path('blogs/<int:pk>/', BlogInstanceView.as_view(), name='blog_instance'),
    path('blogs/search/', BlogSearchView.as_view(), name='blog_search'),
    path('blogs/filter/', BlogFilterView.as_view(), name='blog_filter'),
    path('tags/', TagListView.as_view(), name='tag_list'),
    path('authors/', AuthorListView.as_view(), name='author_list'),
]