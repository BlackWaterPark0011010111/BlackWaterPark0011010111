from django.urls import path
from . import views

urlpatterns = [
   path('', views.home ),
   path('create_user', views.new_user)
]