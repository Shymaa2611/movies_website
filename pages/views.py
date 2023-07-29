from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Movie,Rating

def index(request):
     movies=Movie.objects.all()
     context={
          'movies':movies[:4],
          'top_rated':movies[4:8],
          'best_Seller':movies[8:]
     }
     return render(request,'pages/index.html',context)

def detail(request,id):
     movies=Movie.objects.get(id=id)
     context={
          'movie':movies,
          'best_Seller':Movie.objects.all()[8:]
     }
     return render(request,'pages/detail.html',context)

def movie(request):
     movies=Movie.objects.all()
     context={
          'movies':movies[:4],
          'top_rated':movies[4:8],
          'best_Seller':movies[8:]
     }
     return render(request,'pages/movies.html',context)





