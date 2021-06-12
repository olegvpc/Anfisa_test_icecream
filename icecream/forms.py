from django.forms import ModelForm
from .models import Icecream, Friend


class IcecreamForm(ModelForm):
    class Meta:
        model = Icecream
        fields = ("name", "description")

class FriendForm(ModelForm):
    class Meta:
        model = Friend
        fields = ("friend_name", "friend_city")

