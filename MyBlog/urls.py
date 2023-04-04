from django.urls import path
from .views import LandingPageView, HomePageView, DetailPageView, PostCreateView, PostUpdateView, PostDeleteView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns= [ 
    path('', LandingPageView.as_view(), name = 'index'),             
    path('home/', HomePageView.as_view(), name='home'),
    path('post/<int:id>/', DetailPageView.as_view(), name='post_detail'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('register/', views.register, name='register'),

]