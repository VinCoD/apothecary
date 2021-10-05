from django.urls import path
from . import views

app_name = 'page'

urlpatterns = [
    path('', views.index, name="home"),
    path('available_meds/', views.available_meds, name="available_meds")
]