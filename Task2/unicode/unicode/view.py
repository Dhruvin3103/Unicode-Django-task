from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from .import task1
def unicode(request):
    return render(request,'home.html',{})


def task(request, id1,id2):
    l=task1.task2(id1,id2)
    print(l)
    return JsonResponse(l,safe=False)