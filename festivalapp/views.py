from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Fest

def home(request):
    fests = Fest.objects 
    return render(request, 'home.html', {'fests' : fests})

def lost(request):
    losts = Fest.objects
    return render(request, 'lost.html', {'losts' : losts})

def talk(request):
    talks = Fest.objects
    return render(request, 'talk.html', {'talks' : talks})

def detail(request, fest_id) :
    details = get_object_or_404(Fest, pk=fest_id)
    return render(request, 'detail.html', {'details' : details })

def new(request):
    return render(request, 'new.html')

def create(request):
    fest = Fest()
    fest.title = request.GET['title']
    fest.body = request.GET['body']
    fest.pub_date = timezone.datetime.now()
    fest.save()
    return redirect('/fest/'+str(fest.id))

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

    