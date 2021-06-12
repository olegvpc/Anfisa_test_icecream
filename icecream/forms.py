from django.forms import ModelForm
from .models import Icecream


class IcecreamForm(ModelForm):
    class Meta:
        model = Icecream
        fields = ("name", "description")
