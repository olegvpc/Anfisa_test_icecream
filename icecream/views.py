from django.shortcuts import render, redirect

from .forms import IcecreamForm
from .models import Icecream


def icecream_detail_pk(request, pk):
    name = icecream_db[pk]['name']
    description = icecream_db[pk]['description']
    context = {
        'name': name,
        'description': description,
    }
    return render(request, 'icecream/icecream-detail.html', context)


def icecream_detail(request):

    icecreams = Icecream.objects.all()
    return render(request, 'icecream/icecream-detail.html', {'icecreams': icecreams})


def icecream_new(request):
    if request.method == "POST":
        form = IcecreamForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('index')
    else:
        form = IcecreamForm()
    return render(request, 'icecream/icecream-new.html', {'form':form})