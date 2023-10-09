from django.urls import path
from . import views

urlpatterns = [
    #URL-паттерн для вашей страницы
    path('example/', views.example_page, name='example_page'),

    
]
