from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Movie,Rating,Genre

def index(request):
     movies=Movie.objects.all()
     context={
          'movies':movies[:4],
          'top_rated':movies.order_by('-rated')[:8],
          'best_Seller':movies[8:]
     }
     return render(request,'pages/index.html',context)

def detail(request,id):
     movies=Movie.objects.get(id=id)
     genre=Genre.objects.all()
     context={
          'movie':movies,
          'best_Seller':Movie.objects.all()[8:]
     }
     return render(request,'pages/detail.html',context)

def movie(request):
     movies=Movie.objects.all()
     context={
          'movies':movies[:4],
          'top_rated':movies.order_by('-rated')[:8],
          'best_Seller':movies[8:]
     }
     return render(request,'pages/movies.html',context)
def pricing(request):
     movies=Movie.objects.all()
     context={
          'movies':movies[:4],
          'top_rated':movies.order_by('-rated')[:8],
          'best_Seller':movies[8:]
     }
     return render(request,'pages/pricing.html',context)

def web_Series(request):
     movies=Movie.objects.all()
     context={
          'movies':movies.filter(genre__exact=3)
     }
     return render(request,'pages/webSeries.html',context)

def Tv_show(request,id):
     movies=Movie.objects.get(id=id)
     genre=Genre.objects.all()
     context={
          'movie':movies,
          'best_Seller':Movie.objects.all()[8:]
     }
     return render(request,'pages/watchnow.html',context)









