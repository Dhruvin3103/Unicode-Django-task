from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .import apis
from .apis import find
from .models import searchs
# Create your views here.
def store(s,c,t):

    search  = searchs(search_title=s,title=c,link=t)
    search.save()

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

    if(len(searchs.objects.all())==0):
        if (dt != ''):
            store(dt, c, t)
    else:
        for i in searchs.objects.all():
            w=0
            if(i.search_title==dt):
                i.count+=1
                w+=1
                i.save()
                break

        if(dt != '' and w==0):
                store(dt, c, t)



    db={'data':zip(t,c,q)}
    return render(request,'taskthree.html',db)