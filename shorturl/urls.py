from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.url_shortener, name='index'),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('view-urls/', views.view_urls, name='view_urls'),
    path('<str:shortened_part>', views.view_shorturl, name='shorturl'),
]
