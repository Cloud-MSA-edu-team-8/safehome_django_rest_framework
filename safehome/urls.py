from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListCrime.as_view()),
    path('<int:pk>/', views.DetailCrime.as_view()),

]