from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('<int:blog_id>/', views.blog_detail, name='blog_detail'),
]