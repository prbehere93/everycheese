from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import cheese

#a simple view which lists all the cheeses on a single page
class CheeseListView(ListView):
    model=cheese

#for helping the user view the model in the frontend
class CheeseDetailView(DetailView):
    model=cheese