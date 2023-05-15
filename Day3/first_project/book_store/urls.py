from django.urls import path
from .views import index, book_store_list, book_store_detail, book_store_delete, book_store_update

app_name = 'book_store'

# http://localhost:8000/post/2/comment/1
urlpatterns = [
    path('index', index, name='book_store-index'),
    path('book_store_list/', book_store_list, name="book_store-list"),
    path('book_store_detail/<int:task_id>', book_store_detail, name="book_store-detail"),
    path('book_store_delete/<int:task_id>', book_store_delete, name="book_store-delete"),
    path('book_store_update/<int:task_id>', book_store_update, name="book_store-update")
]
