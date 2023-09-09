from django.db import models

from account_module.models import User
from movies_module.models import Movie
from cinema_module.models import Cinema


# Create your models here.
class ShowTime(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    price = models.IntegerField(default=20000)
    free_seats = models.IntegerField()
    salable_seats = models.IntegerField()

    SALE_NOT_STARTED = 1
    SALE_OPEN = 2
    TICKETS_SOLD = 3
    SALE_CLOSED = 4
    MOVIE_PLAYED = 5
    SHOW_CANCELED = 6

    status_choices = (
        (SALE_NOT_STARTED, 'sale not started'),
        (SALE_OPEN, 'sale open'),
        (TICKETS_SOLD, 'tickets sold'),
        (SALE_CLOSED, 'sale closed'),
        (MOVIE_PLAYED, 'movie played'),
        (SHOW_CANCELED, 'show canceled'),
    )

    status = models.IntegerField(choices=status_choices)

    def get_price(self):
        return f'{self.price} dollars'

    def reserve_seat(self, seat_count):
        assert isinstance(seat_count, int) and seat_count > 0, 'The number of seat should more than 0'
        assert self.status == ShowTime.SALE_OPEN, 'Sale is not open'
        assert self.free_seats >= seat_count, 'NO enough free seat'
        self.free_seats -= seat_count
        if self.free_seats == 0:
            self.status = ShowTime.TICKETS_SOLD
        self.save()

    def __str__(self):
        return f'{self.movie.name} {self.cinema.name} {self.start_time}'


class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    showtime = models.ForeignKey(ShowTime, on_delete=models.CASCADE)
    seat_count = models.IntegerField()
    order_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Ticket count:{self.seat_count} user: {self.user.username} movie:{self.showtime.movie}'
