from django.urls import path

from . import views

urlpatterns = [
    path('alcohol/', views.ListAlcohol.as_view()),
    path('alcohol/<int:pk>/', views.DetailAlcohol.as_view()),

    path('children/', views.ListChildren.as_view()),
    path('children/<int:pk>/', views.DetailChildren.as_view()),

    path('crime/', views.ListCrime.as_view()),
    path('crime/<int:pk>/', views.DetailCrime.as_view()),

    path('fire/', views.ListFire.as_view()),
    path('fire/<int:pk>/', views.DetailFire.as_view()),

    path('flood/', views.ListFlood.as_view()),
    path('flood/<int:pk>/', views.DetailFlood.as_view()),

    path('house/', views.ListHouse.as_view()),
    path('house/<int:pk>/', views.DetailHouse.as_view()),

    path('population/', views.ListPopulation.as_view()),
    path('population/<int:pk>/', views.DetailPopulation.as_view()),

    path('total/', views.ListTotal.as_view()),
    path('total/<int:pk>/', views.DetailTotal.as_view()),

    path('rate/', views.ListTotalRate.as_view()),
    path('rate/<int:pk>/', views.DetailTotalRate.as_view()),

    path('svgd/', views.ListSvgd.as_view()),
    path('svgd/<int:pk>/', views.DetailSvgd.as_view())
]
