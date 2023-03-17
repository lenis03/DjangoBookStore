from django.urls import path

from . import views
urlpatterns = [
    path('', views.BookListViews.as_view(), name='book_list'),

]