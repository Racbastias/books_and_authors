from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('authors', views.authors),
    path('books', views.books),
    path('add_author', views.add_author),
    path('add_authors', views.add_authors),
    path('add_book', views.add_book),
    path('add_books', views.add_books),
    path('del_books', views.del_books),
    path('books/<book_id>', views.book),
    path('author/<author_id>', views.author),
    path('delete/<author_id>/<book_id>', views.delete),
]
