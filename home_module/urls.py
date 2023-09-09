from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home_page'),
    path('not-yet-completed', views.not_yet_completed, name='not_yet_completed')
]
