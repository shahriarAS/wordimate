from django.urls import path
from word import views

urlpatterns = [
		path('', views.Home, name="Home"),
		path('add/', views.AddNew, name="AddNew"),
			]