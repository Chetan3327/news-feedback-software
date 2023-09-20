from django.urls import path
from . import views
from django.http import HttpResponse

urlpatterns = [
    path('', views.home),
    path('predict/', views.predict),
    path('predict_api/', views.predict_api),
]