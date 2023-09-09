from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from .models import ShowTime, Ticket
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ShowTimeSearchForm


# Create your views here.


class Ticketing(LoginRequiredMixin, View):
    def get(self, request):
        show_times = ShowTime.objects.all()
        show_times_search_form = ShowTimeSearchForm(request.GET)
        if show_times_search_form.is_valid():

            movie_name = show_times_search_form.cleaned_data.get('movie_name')
            if movie_name is not None:
                show_times = show_times.filter(movie__name__icontains=movie_name)
            min_length = show_times_search_form.cleaned_data.get('movie_length_min')
            if min_length is not None:
                show_times = show_times.filter(movie__length__gte=min_length)
            max_length = show_times_search_form.cleaned_data.get('movie_length_max')
            if max_length is not None:
                show_times = show_times.filter(movie__length__lte=max_length)
            cinemas = show_times_search_form.cleaned_data.get('cinemas')
            if cinemas is not None:
                show_times = show_times.filter(cinema=cinemas)
            min_price, max_price = show_times_search_form.get_price_boundaries()
            if min_price is not None:
                show_times = show_times.filter(price__gte=min_price)
            if max_price is not None:
                show_times = show_times.filter(price__lte=max_price)

            show_times = show_times.order_by('start_time')

            context = {
                'show_times': show_times,
                'show_time_search_form': show_times_search_form,
            }
            return render(request, 'ticketing_module/ticketing_page.html', context)

        else:
            context = {
                'show_times': show_times,
                'show_time_search_form': show_times_search_form,
            }
            return render(request, 'ticketing_module/ticketing_page.html', context)


class TicketingDetail(View):
    def get(self, request, pk):
        show_time = ShowTime.objects.filter(id=pk).first()
        context = {
            'show_time': show_time
        }
        return render(request, 'ticketing_module/ticketing_detail_page.html', context)

    def post(self, request, pk):
        show_time = ShowTime.objects.filter(id=pk).first()
        seat_count = 2
        try:
            assert show_time.status == show_time.SALE_OPEN, 'ticket sales is not possible'
            assert show_time.free_seats >= seat_count, 'there is not enough empty seat'
            total_price = seat_count * show_time.price
            assert request.user.spend(total_price), 'you dont have enough money to buy ticket'
            show_time.reserve_seat(seat_count)
            new_ticket = Ticket(user=request.user, showtime=show_time, seat_count=seat_count)
            new_ticket.save()

        except Exception as e:
            context = {
                'show_time': show_time,
                'error': str(e)
            }
            return render(request, 'ticketing_module/ticketing_detail_page.html', context)

        else:
            return HttpResponseRedirect(reverse('ticket_detail', kwargs={'pk': new_ticket.id}))


class TicketsList(View):
    def get(self, request):
        tickets = Ticket.objects.filter(user_id=request.user.id).order_by('-order_time')
        context = {
            'tickets': tickets
        }
        return render(request, 'ticketing_module/tickets_list_page.html', context)


class TicketDetail(View):
    def get(self, request, pk):
        detail = Ticket.objects.filter(user_id=request.user.id, id=pk).first()
        context = {
            'detail': detail
        }
        return render(request, 'ticketing_module/ticket_detail_page.html', context)
