from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.new, name='new'), 
    path('create', views.create, name='create'),
    path('detail/<int:note_id>', views.detail, name='detail'),
    path('edit/<int:note_id>', views.edit, name='edit'),
    path('update/<int:note_id>', views.update, name='update'),
    path('delete/<int:note_id>', views.delete, name='delete'),
]
