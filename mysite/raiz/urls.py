from django.urls import path
from . import views

app_name = 'raiz'
urlpatterns = [
    path('', views.index, name = 'index'),
]
#path('', views.index, name = 'index'),