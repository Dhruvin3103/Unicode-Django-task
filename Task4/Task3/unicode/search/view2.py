from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import searchs

def top(request):
    d = []
    n=[]
    for i in searchs.objects.all().order_by('-count'):
        d.append(i.search_title)
        n.append(i.count)
    c={'file':zip(d[0:3],n[0:3])}


    return render(request,'top3.html',c)

def delete(request):
    d=request.GET.get('del','off')

    if(d!='off'):
        m=searchs.objects.all()
        m.delete()
        return render(request,'home.html',{})
