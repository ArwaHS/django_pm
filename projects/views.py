from django.shortcuts import render
from django.views.generic import ListView
from . import models
# Create your views here.

class ProjectListView(ListView):
    model =models.Project
    tamplate_name = 'project/list.html'
