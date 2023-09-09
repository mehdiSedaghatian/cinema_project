from django.urls import path
from . import views

urlpatterns = [
    path('', views.Ticketing.as_view(), name='ticketing'),
    path('tickets-list', views.TicketsList.as_view(), name='tickets_list'),
    path('<pk>', views.TicketingDetail.as_view(), name='ticketing_detail'),
    path('detail/<pk>', views.TicketDetail.as_view(), name='ticket_detail'),
]