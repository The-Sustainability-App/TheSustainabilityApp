from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog_page, name='blog'),
    path('app/', views.app, name='app'),
    path('about/', views.about, name='about'),
]
