from django.urls import path

from new_app import views

urlpatterns = [
    path('', views.read, name=""),
    path('create', views.create, name="create"),
    path('updt/<int:id>/', views.update, name="updt"),
    path('delt/<int:id>/', views.delete, name="delt"),
]
