from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import TemplateView, View, ListView, DetailView
from .models import Genre, MovieGallery, Movie, MovieComments, Like, Dislike, MovieReview
from django.db.models import Q, Count
from .forms import MovieNameForm
from django.core.paginator import Paginator
from utils.http_service import get_client_ip


# Create your views here.


# class MovieListView(ListView):
#     template_name = 'movies_module/movie_list_page.html'
#     model = Movie
#     paginate_by = 6
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super(MovieListView, self).get_context_data()
#         movie_name_form = MovieNameForm()
#         genre_form = GenreForm()
#         imdb_form = ImdbForm()
#         year_form = YearForm()
#
#         movie_list = Movie.objects.filter(is_active=True)
#
#         # movie_list = Movie.objects.filter(genre__name=genre)
#
#         genres = Genre.objects.all()
#         number_of_genre = len(genres)
#
#         context['movie_name_form'] = movie_name_form
#         context['genre_form'] = genre_form
#         context['imdb_form'] = imdb_form
#         context['year_form'] = year_form
#         context['movie_list'] = movie_list
#         context['genres'] = genres
#         context['number_of_genre'] = number_of_genre
#         return context
#
#     def get_queryset(self):
#         query = super(MovieListView, self).get_queryset()
#         request: HttpRequest = self.request
#         year_form = YearForm(request.GET)
#         imdb_form = ImdbForm(request.GET)
#         genre_form = GenreForm(request.GET)
#         movie_name_form = MovieNameForm(request.GET)
#
#         # if imdb_form.is_valid() and year_form.is_valid() and genre_form.is_valid() and movie_name_form.is_valid():
#         start_year = year_form.cleaned_data.get('start_year')
#         end_year = year_form.cleaned_data.get('end_year')
#         imdb_start = imdb_form.cleaned_data.get('imdb_start')
#         imdb_end = imdb_form.cleaned_data.get('imdb_end')
#         genre_title = genre_form.cleaned_data.get('genre')
#         movie_name = movie_name_form.cleaned_data.get('movie_name')
#         if imdb_start and imdb_end and start_year and end_year and genre_title and movie_name is not None:
#             movie_list = query.filter(Q(imdb__gte=imdb_start) & Q(imdb__lte=imdb_end) & Q(year__gte=start_year) & Q(year__lte=end_year) & Q(genre__name__icontains=genre_title) & Q(name__icontains=movie_name))
#             query = movie_list
#
#         return query


class MovieListView(View):
    def get(self, request):

        movie_name_form = MovieNameForm(request.GET)

        if movie_name_form.is_valid():
            movie_name = movie_name_form.cleaned_data.get('movie_name')
            if movie_name is not None:
                movie_list = Movie.objects.filter(name__icontains=movie_name)
                genres = Genre.objects.filter(is_active=True)
                number_of_genre = len(genres)
                p = Paginator(movie_list, 6)
                page = request.GET.get('page')
                movie_list = p.get_page(page)

                context = {
                    'movie_name_form': movie_name_form,
                    'movie_list': movie_list,
                    'genres': genres,
                    'number_of_genre': number_of_genre,

                }
                return render(request, 'movies_module/movie_list_page.html', context)

        else:

            genres = Genre.objects.filter(is_active=True)
            number_of_genre = len(genres)
            movie_list = Movie.objects.filter(is_active=True)

            context = {
                'movie_name_form': movie_name_form,
                'movie_list': movie_list,
                'genres': genres,
                'number_of_genre': number_of_genre
            }
            return render(request, 'movies_module/movie_list_page.html', context)


class MovieGenreView(View):
    def get(self, request, genre):
        movie_list = Movie.objects.filter(genre__name=genre)

        genres = Genre.objects.filter(is_active=True)
        p = Paginator(movie_list, 6)
        page = request.GET.get('page')
        movie_list = p.get_page(page)

        context = {
            'movie_list': movie_list,
            'genres': genres,

        }
        return render(request, 'movies_module/movie_list_page.html', context)


class MovieDitailView(View):
    def get(self, request, pk):
        galleries = MovieGallery.objects.filter(movie__id=pk).all()
        movie = Movie.objects.filter(id=pk).first()
        movie_genres = movie.genre.all()
        genres = Genre.objects.filter(id__in=movie_genres).exclude(id=1).all()[:1]
        you_may_like = Movie.objects.filter(genre__id__in=genres).exclude(id=pk).order_by('-imdb').all()
        comments = MovieComments.objects.filter(movie_id=movie.id).order_by('-create_date')
        reviews = MovieReview.objects.filter(movie_id=movie.id).order_by('-create_date')
        context = {
            'movie': movie,
            'galleries': galleries,
            'you_may_like': you_may_like,
            'comments': comments,
            'reviews': reviews

        }
        return render(request, 'movies_module/movie_detail_page.html', context)


def add_movie_comment(request: HttpRequest):
    if request.user.is_authenticated:
        movie_comment = request.GET.get('movie_comment')
        movie_id = request.GET.get('movie_id')
        movie_user = request.user.id
        new_comments = MovieComments(text=movie_comment, movie_id=movie_id, user_id=movie_user)
        new_comments.save()
        comments = MovieComments.objects.filter(movie_id=movie_id).order_by('-create_date')
        movie = Movie.objects.filter(id=movie_id).first()

        context = {

            'comments': comments,
            'movie': movie,
        }
        return render(request, 'movies_module/includes/movie_comments_partial.html', context)


def like(request):
    comment_id = request.GET.get('comment_id')
    movie_id = request.GET.get('movie_id')
    user_ip = get_client_ip(request)
    comment = MovieComments.objects.filter(id=comment_id).first()
    has_been_liked = Like.objects.filter(ip=user_ip, user=request.user, movie_comment=comment).first()

    if has_been_liked is None:
        new_like = Like(ip=user_ip, user=request.user, movie_comment=comment)
        new_like.save()
        comment.num_of_like = comment.num_of_like + 1
        comment.save()
        comments = MovieComments.objects.filter(movie_id=movie_id).order_by('-create_date')
        movie = Movie.objects.filter(id=movie_id).first()

        context = {
            'comments': comments,
            'movie': movie,
        }
        return render(request, 'movies_module/includes/like_and_dislike_partial.html', context)
    else:
        has_been_liked.delete()
        comment.num_of_like = comment.num_of_like - 1
        comment.save()
        comments = MovieComments.objects.filter(movie_id=movie_id).order_by('-create_date')
        movie = Movie.objects.filter(id=movie_id).first()

        context = {
            'comments': comments,
            'movie': movie,
        }
        return render(request, 'movies_module/includes/like_and_dislike_partial.html', context)


def dislike(request):
    comment_id = request.GET.get('comment_id')
    movie_id = request.GET.get('movie_id')
    user = request.user.id
    user_ip = get_client_ip(request)

    has_been_disliked = Dislike.objects.filter(movie_comment_id=comment_id, user_id=user, ip=user_ip).first()
    comment = MovieComments.objects.filter(id=comment_id).first()
    if has_been_disliked is None:
        new_dislike = Dislike(ip=user_ip, user=request.user, movie_comment=comment)
        new_dislike.save()
        comment.num_of_dislike = comment.num_of_dislike + 1
        comment.save()
        comments = MovieComments.objects.filter(movie_id=movie_id).order_by('-create_date')
        movie = Movie.objects.filter(id=movie_id).first()

        context = {
            'comments': comments,
            'movie': movie,
        }
        return render(request, 'movies_module/includes/like_and_dislike_partial.html', context)
    else:
        has_been_disliked.delete()
        comment.num_of_dislike = comment.num_of_dislike - 1
        comment.save()
        comments = MovieComments.objects.filter(movie_id=movie_id).order_by('-create_date')
        movie = Movie.objects.filter(id=movie_id).first()

        context = {
            'comments': comments,
            'movie': movie,
        }
        return render(request, 'movies_module/includes/like_and_dislike_partial.html', context)


def add_movie_review(request):
    review_title = request.GET.get('review_title')
    review_text = request.GET.get('review_text')
    review_rate = request.GET.get('review_rate')
    movie_id = request.GET.get('movie_id')
    movie = Movie.objects.filter(id=movie_id).first()

    new_review = MovieReview(title=review_title, text=review_text, user=request.user, movie=movie, rate=review_rate)
    new_review.save()
    reviews = MovieReview.objects.filter(movie_id=movie_id).order_by('-create_date')
    movie = Movie.objects.filter(id=movie_id).first()
    context = {

        'reviews': reviews,
        'movie': movie

    }
    return render(request, 'movies_module/includes/movie_reviews_partial.html', context)

# to movie list ye dropdown mizaram va bar asas imdb va tedad bazdid va jdid tarin daste bandi mikonam
