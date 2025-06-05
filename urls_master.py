from django.urls import path

from news.views import article_detail_view, list_view

urlpatterns = [
        # path("articles/<int:pk>", article_detail_view, name="article-detail"),
        path("articles_nuovo/<int:pk>", article_detail_view, name="article-detail"),
        path("list-news/", list_view, name="list-news")
]        
