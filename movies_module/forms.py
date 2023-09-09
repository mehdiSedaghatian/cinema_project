from django import forms


# class ImdbForm(forms.Form):
#     imdb_start = forms.FloatField(
#         label='imdb=> ',
#         widget=forms.NumberInput(attrs={
#             'class': 'imdb_input',
#
#         }),
#
#     )
#     imdb_end = forms.FloatField(
#         label='to',
#         widget=forms.NumberInput(attrs={
#             'class': 'imdb_input',
#
#         }),
#
#     )
#
#
# class YearForm(forms.Form):
#     start_year = forms.IntegerField(
#         label='Year=> ',
#         widget=forms.NumberInput(attrs={
#             'class': 'year_input',
#
#         }),
#
#     )
#     end_year = forms.IntegerField(
#         label='to',
#         widget=forms.NumberInput(attrs={
#             'class': 'year_input',
#
#         }),
#
#     )
#
#
# class GenreForm(forms.Form):
#     genre = forms.CharField(
#         label='genre',
#         widget=forms.TextInput(attrs={
#             'class': 'year_input',
#
#         })
#
#     )


class MovieNameForm(forms.Form):
    movie_name = forms.CharField(
        label='movie name',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form control bg-red',
            'placeholder': 'Movie Name',
            'style': 'color:gray; height:20px',
            'id': 'search_movie_input'

        })

    )
