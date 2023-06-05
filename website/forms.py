from django import forms
from django.core.exceptions import ValidationError
from .models import Order


class OrderForm(forms.Form):
    adress = forms.CharField(
        label="Адрес, куда доставлять",
        required=False,
        max_length=120
    )
    tomato_type = forms.ChoiceField(
        choices = Order.TOMATO_TYPE,
        label="Вид помидорки",
        required=True,
    )

    # class Meta:
    #     model = User
    #     fields = [
    #         "name",
    #         "email",
    #         "adress",
    #         # "contact",
    #         # "email_digest_type",
    #     ]
