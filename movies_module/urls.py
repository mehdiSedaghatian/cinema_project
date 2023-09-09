from django.urls import path
from . import views

urlpatterns = [
    path('movie-list/', views.MovieListView.as_view(), name='movie_list'),
    path('genre/<genre>', views.MovieGenreView.as_view(), name='movie_genre'),
    path('<pk>/', views.MovieDitailView.as_view(), name='movie_detail'),
    path('add-movie-comment', views.add_movie_comment, name='add_movie_comment'),
    path('add-movie-review', views.add_movie_review, name='add_movie_review'),
    path('like', views.like, name='like'),
    path('dislike', views.dislike, name='dislike'),

]
