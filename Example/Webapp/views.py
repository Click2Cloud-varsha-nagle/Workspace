from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Ex(request):
    return HttpResponse("<h1>This Text is visible or not</h1>")