from django.urls import path
# Import views from current base app folder
from . import views

# Create base app urls
urlpatterns = [
    path('', views.hello, name='home'),
    path('add_book/', views.addBook, name='add'),
    path('edit_book/<str:id>', views.editBook, name='edit'),
    path('delete_book/<str:id>', views.deleteBook, name='edit'),
    path('<str:id>/', views.displayById, name="identifier"),
]