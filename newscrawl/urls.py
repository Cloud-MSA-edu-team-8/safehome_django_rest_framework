from django.urls import path

from . import views

urlpatterns = [
    path('news/', views.ListNews.as_view()),
    path('news/<int:pk>/', views.DetailNews.as_view()),
]
