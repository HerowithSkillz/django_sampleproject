
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_coffees, name='all_coffee'),
    path('<int:coffee_id>/', views.coffee_details, name='coffee_detail'),
]