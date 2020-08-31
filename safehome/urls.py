from django.urls import path

from . import views

urlpatterns = [
   path('region/', views.ListRegion.as_view()),
   path('region/<str:pk>/', views.DetailRegion.as_view()),

   path('alcohol/', views.ListAlcohol.as_view()),
   path('alcohol/<str:pk>/', views.DetailAlcohol.as_view()),

   path('children/', views.ListChildren.as_view()),
   path('children/<str:pk>/', views.DetailChildren.as_view()),

   path('crime/', views.ListCrime.as_view()),
   path('crime/<str:pk>/', views.DetailCrime.as_view()),

   path('fire/', views.ListFire.as_view()),
   path('fire/<str:pk>/', views.DetailFire.as_view()),

   path('flood/', views.ListFlood.as_view()),
   path('flood/<str:pk>/', views.DetailFlood.as_view()),

   path('house/', views.ListHouse.as_view()),
   path('house/<str:pk>/', views.DetailHouse.as_view()),

   path('population/', views.ListPopulation.as_view()),
   path('population/<str:pk>/', views.DetailPopulation.as_view()),

   path('total/', views.ListTotal.as_view()),
   path('total/<str:pk>/', views.DetailTotal.as_view()),

   path('rate/', views.ListTotalRate.as_view()),
   path('rate/<str:pk>/', views.DetailTotalRate.as_view()),

   path('draw_data/', views.ListDrawdata.as_view()),
   path('draw_data/<str:pk>/', views.DetailDrawdata.as_view())
]
