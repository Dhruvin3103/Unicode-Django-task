from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .import apis
from .apis import find
# Create your views here.
def task3(request):
    s = request.GET.get('submit', 0)
    dt = request.GET.get('data','')
    d=find(dt)
    l1=d["results"]
    c = []
    t=[]
    q=[]
    for j in range(len(l1)):
        t.append(l1[j]["title"])
        c.append(l1[j]['link'])
        q.append(l1[j]['description'])
    db={'data':zip(t,c,q)}
    return render(request,'taskthree.html',db)