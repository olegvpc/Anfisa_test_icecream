from django.shortcuts import render
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


# from django.http import HttpResponse
#
# def index(request):
#     return HttpResponse('АНФИСА ДЛЯ ДРУЗЕЙ')