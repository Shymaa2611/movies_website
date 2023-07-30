from django.urls import path

from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('movie/', views.movie, name='movie'),
   path('pricing/', views.pricing, name='pricing'),
   path('webSeries/', views.web_Series, name='webSeries'),
   path('detail/<int:id>/', views.detail, name='detail'),
   path('watchnow/<int:id>/', views.Tv_show, name='watchnow'),

]

