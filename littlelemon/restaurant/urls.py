#define URL route for index() view
from django.urls import path, include
from . import views



urlpatterns = [

    path('', views.index, name='index'),
    path('menu-items/', views.MenuView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
]