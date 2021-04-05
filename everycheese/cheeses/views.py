from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import cheese
from django.urls import reverse

#a simple view which lists all the cheeses on a single page
class CheeseListView(ListView):
    model=cheese

#for helping the user view the model in the frontend
class CheeseDetailView(DetailView):
    model=cheese

#For creating cheese model objects from the fromtend
class CheeseCreateView(CreateView):
    model=cheese
    fields=['name','description','firmness','country_of_origin']

