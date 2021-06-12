from django.shortcuts import render, redirect

from icecream.forms import FriendForm
from icecream.models import Icecream, Friend
from .services import what_weather


def index(request):
    friends = Friend.objects.all()
    icecreams = Icecream.objects.all()
    if request.method == "POST":
        friend_choice = request.POST['friend']
        ice_choice = request.POST['icecream']
        friend = Friend.objects.get(friend_name=friend_choice)
        city = friend.friend_city
        weather = what_weather(city)
        print(city)
        return render(request, 'homepage/index.html', {'friends':friends,
                  'icecreams':icecreams, 'friend_choice': friend_choice,
                  'ice_choice': ice_choice, 'city':city, 'weather':weather, 'mode':'post'})
    return render(request, 'homepage/index.html', {'friends': friends,
                                                   'icecreams': icecreams, 'mode': 'get'})

def new_friend(request):
    if request.method == 'POST':
        form = FriendForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    form = FriendForm()
    return render(request, "homepage/friend.html", {"form":form})

# from django.http import HttpResponse
#
# def index(request):
#     return HttpResponse('АНФИСА ДЛЯ ДРУЗЕЙ')