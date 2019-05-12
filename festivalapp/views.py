from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Fest
from .models import Lost

def home(request):
    fests = Fest.objects 
    return render(request, 'home.html', {'fests' : fests})

def lost(request):
    losts = Lost.objects
    return render(request, 'lost.html', {'losts' : losts})

def talk(request):
    talks = Fest.objects
    return render(request, 'talk.html', {'talks' : talks})

def detail(request, fest_id) :
    details = get_object_or_404(Fest, pk=fest_id)
    return render(request, 'detail.html', {'details' : details })

def detail_lost(request, lost_id) :
    details_lost = get_object_or_404(Lost, pk=lost_id)
    return render(request, 'detail_lost.html', {'details_lost' : details_lost })


def new(request):
    return render(request, 'new.html')

def new_lost(request):
    return render(request, 'new_lost.html')


def create(request):
    fest = Fest()
    fest.title = request.GET['title']
    fest.writer = request.GET['writer']
    fest.body = request.GET['body']
    fest.pub_date = timezone.datetime.now()
    fest.save()
    return redirect('/fest/'+str(fest.id))

def create_lost(request):
    lost = Lost()
    lost.title2 = request.GET['title']
    lost.body2 = request.GET['body']
    lost.writer2 = request.GET['writer']
    lost.pub_date2 = timezone.datetime.now()
    lost.save()
    return redirect('/fest_lost/' +str(lost.id))

def delete(request, delete_fest_id):
    delete_fest = get_object_or_404(Fest, pk=delete_fest_id)
    delete_fest.delete()
    return redirect('home')

def edit(request, edit_fest_id):
    edit_fest = get_object_or_404(Fest, pk=edit_fest_id)
    return render(request, 'edit.html', {'fest': edit_fest})

def update(request, update_fest_id):
    update_fest = get_object_or_404(Fest, pk= update_fest_id)
    update_fest.title = request.GET["title"]
    update_fest.writer = request.GET['writer']
    update_fest.body = request.GET['body']
    update_fest.save()
    return redirect('/fest/'+str(update_fest.id))

def delete_lost(request, delete_lost_id):
    delete_lost = get_object_or_404(Lost, pk=delete_lost_id)
    delete_lost.delete()
    return redirect('home')

def edit_lost(request, edit_lost_id):
    edit_lost = get_object_or_404(Lost, pk=edit_lost_id)
    return render(request, 'edit_lost.html', {'lost': edit_lost})

def update_lost(request, update_lost_id):
    update_lost = get_object_or_404(Lost, pk= update_lost_id)
    update_lost.title2 = request.GET["title"]
    update_lost.writer2 = request.GET['writer']
    update_lost.body2 = request.GET['body']
    update_lost.save()
    return redirect('/fest_lost/'+str(update_lost.id))

    