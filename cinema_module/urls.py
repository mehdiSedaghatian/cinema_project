from django.urls import path
from . import views

urlpatterns = [
    path('cinema-list', views.CinemaListView.as_view(), name='cinema_list')
]
