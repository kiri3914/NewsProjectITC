from django.urls import path
from .views import index, product, news_detail, create_news, delete_news, edit_news

urlpatterns = [
    path("", index, name="index"),
    path("products/", product, name="product"),
    path("news/<int:id>/", news_detail, name="news_detail"),
    path("create_news/", create_news, name="create_news"),
    path("delete_news/<int:id>/", delete_news, name="delete_news"),
    path("edit_news/<int:id>/", edit_news, name="edit_news"),
]