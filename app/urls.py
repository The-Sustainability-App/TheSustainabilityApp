from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('app/', views.app, name='app'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog_page.as_view(), name='blog'),
    path('blog/<slug:slug>/', views.blog_post_detail.as_view(), name='post_detail'),
]
