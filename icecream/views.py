from django.shortcuts import render
from .models import icecream_db

def icecream_detail(request, pk):
    name = icecream_db[pk]['name']
    description = icecream_db[pk]['description']
    context = {
        'name': name,
        'description': description,
    }
    return render(request, 'icecream/icecream-detail.html', context)

def icecream_new(request):
    new_icecream = f'тут будет новое мороженое<br>'
    new_description = ''
    new_ice_db = {}
    inform_me=''
    if request.method == 'POST':
        new_icecream = request.POST['new_icecream']
        new_description = request.POST['new_description']
        #last_car=len(icecream_db)
        new_ice_db['name']=new_icecream
        new_ice_db['description']=new_description
        inform_me= f'<strong>{new_icecream}</strong> ДОБАВЛЕНО'
        icecream_db.append(new_ice_db)
    context={
            'new_icecream': new_icecream,
        'inform_me': inform_me,
        }

    return render(request, 'icecream/icecream-new.html', context)