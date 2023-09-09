from django.db import models
from embed_video.fields import EmbedVideoField

from account_module.models import User


# Create your models here.
class Movie(models.Model):
    image = models.ImageField(upload_to='movie_image', null=True, blank=True)
    name = models.CharField(max_length=100)
    imdb = models.FloatField(default=0)
    year = models.IntegerField()
    length = models.IntegerField()
    description = models.TextField()
    director = models.ManyToManyField('Director')
    genre = models.ManyToManyField('Genre')
    country = models.ManyToManyField('Country')
    is_active = models.BooleanField(default=True)
    local_trailer = models.FileField(upload_to='movie_video/', default='movie_video/pexels-vision-plug-15698543_1080p.mp4')
    trailer = EmbedVideoField(null=True, blank=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class MovieGallery(models.Model):
    image = models.ImageField(upload_to='movie_image/gallery/')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, )

    def __str__(self):
        return self.movie.name


class MovieComments(models.Model):
    text = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    num_of_like = models.IntegerField(default=0)
    num_of_dislike = models.IntegerField(default=0)

    def __str__(self):
        return self.movie.name


class Like(models.Model):
    ip = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_comment = models.ForeignKey(MovieComments, on_delete=models.CASCADE)

    def __str__(self):
        return self.movie_comment.text


class Dislike(models.Model):
    ip = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_comment = models.ForeignKey(MovieComments, on_delete=models.CASCADE)

    def __str__(self):
        return self.movie_comment.text


class MovieReview(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rate = models.FloatField()

    def __str__(self):
        return self.movie.name
