from django import forms

from cinema_module.models import Cinema


class ShowTimeSearchForm(forms.Form):
    movie_name = forms.CharField(
        label='Movie name',
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control w-25'

        })

    )
    # sale_is_open = forms.BooleanField(
    #     label='only available for purchase',
    #     required=False,
    #     widget=forms.CheckboxInput()

    # )
    movie_length_min = forms.IntegerField(
        label='min',
        required=False,
        min_value=0,
        max_value=200,
        widget=forms.NumberInput(attrs={
            'class': 'form-control w-25'
        })

    )

    movie_length_max = forms.IntegerField(
        label='max',
        required=False,
        min_value=0,
        max_value=200,
        widget=forms.NumberInput(attrs={
            'class': 'form-control w-25'
        })

    )

    ANY_PRICE = '0'
    PRICE_UNDER_10 = '1'
    PRICE_10_TO_15 = '2'
    PRICE_15_TO_20 = '3'
    PRICE_ABOVE_20 = '4'
    PRICE_LEVEL_CHOICES = (
        (ANY_PRICE, 'any price'),
        (PRICE_UNDER_10, 'price under 10 '),
        (PRICE_10_TO_15, 'price 10 to 15'),
        (PRICE_15_TO_20, 'price 15 to 20'),
        (PRICE_ABOVE_20, 'price above 20'),
    )
    price_level = forms.ChoiceField(
        label='price level',
        required=False,
        choices=PRICE_LEVEL_CHOICES,

    )
    cinemas = forms.ModelChoiceField(queryset=Cinema.objects.all(), required=False, label='Cinemas')

    def get_price_boundaries(self):
        price_level = self.cleaned_data['price_level']
        if price_level == ShowTimeSearchForm.PRICE_UNDER_10:
            return None, 10
        elif price_level == ShowTimeSearchForm.PRICE_10_TO_15:
            return 10, 15
        elif price_level == ShowTimeSearchForm.PRICE_15_TO_20:
            return 15, 20
        elif price_level == ShowTimeSearchForm.PRICE_ABOVE_20:
            return 20, None
        else:
            return None, None
