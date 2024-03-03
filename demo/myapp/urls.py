from django.urls import path
from . import views

urlpatterns = [
    path("", views.home , name="home"),
    path("todos/", views.todos, name="Todos"),
    path("view/", views.my_view, name='my_form'),
    path("show/", views.show_data, name='show_data'),
    # path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
]