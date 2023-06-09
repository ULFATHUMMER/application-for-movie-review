from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm

# Create your views here.


def index(request):
    items = Movie.objects.all()
    context={
        'movie_list':items
    }
    return render(request,"index.html",context)

def detail(request,item_id):
    movie = Movie.objects.get(id=item_id)
    return render(request,"detail.html",{"movie":movie} )
def add(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        desc=request.POST.get('desc',)
        year=request.POST.get('year',)
        image=request.FILES['image']
        movie=Movie(name=name,desc=desc,year=year,image=image)
        movie.save()

    return render(request,'add.html')

def update(request,item_id):
    movie=Movie.objects.get(id=item_id)
    form = MovieForm(request.POST or None, request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request,'edit.html',{"form":form,"movie":movie})

def delete(request,item_id):
    if request.method =='POST':
        movie= Movie.objects.get(id=item_id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')