from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
# from .import api

def home(request):

    return render(request,'home.html',{})