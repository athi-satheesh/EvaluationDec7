from django.urls import path

from new_app import views

urlpatterns = [
    path('', views.read, name="read"),
    path('delt/<int:id>/', views.delete, name="delt"),
]
