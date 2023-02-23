from django.urls import path

from . import views

urlpatterns=[
    path('lista/api/',views.Lista.as_view()),
    path('abogado/api/<int:abogado_id>/', views.listaAbodagosDetail.as_view()),
]