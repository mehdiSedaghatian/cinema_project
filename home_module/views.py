from django.shortcuts import render
from django.views.generic import View
from movies_module.models import Movie


# Create your views here.
def site_header_component(request):
    return render(request, 'shared/site_header_components.html')


def site_footer_component(request):
    return render(request, 'shared/site_footer_components.html')


def not_yet_completed(request):
    return render(request, 'home_module/not_yet_completed.html')


class HomeView(View):
    def get(self, request):
        movies = Movie.objects.all().order_by('-year')
        context = {
            'movies': movies
        }
        return render(request, 'home_module/home_page.html', context)
