from django.urls import path
from .views import HomePageView, DetailPageView, PostCreateView

urlpatterns= [ 
    path('', HomePageView.as_view(), name='home'),
    path('post/<int:id>/', DetailPageView.as_view(), name='post_detail'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
]