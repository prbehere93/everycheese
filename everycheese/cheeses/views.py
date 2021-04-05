from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import cheese

#a simple view which lists all the cheeses on a single page
class CheeseListView(ListView):
    model=cheese

