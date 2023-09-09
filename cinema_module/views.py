from django.shortcuts import render
from django.views.generic import View

from cinema_module.models import Cinema


# Create your views here.

class CinemaListView(View):
    def get(self, request):
        cinemas = Cinema.objects.all()
        context = {
            'cinemas': cinemas
        }

        return render(request, 'cinema_module/cimema_list_page.html', context)
