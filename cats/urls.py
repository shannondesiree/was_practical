from django.urls import path
from cats import views

app_name = 'cats'

urlpatterns = [
    path('', views.index, name='index'),
    path('pets/', views.pets, name='pets'),
]