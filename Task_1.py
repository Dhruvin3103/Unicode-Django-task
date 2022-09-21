#To convert decimal to binary
def db(x):
    y=[]
    while x>=1:
     b=x%2
     y.append(str(b))
     x=x//2
    a=''.join(y[::-1])
    return a
#To check adjacent 1's in binary
def do(b):
    t=0
    for i in range(0,len(b)-1):
        if(b[i]==b[i+1] and b[i]=="1"):
         t=t+1
    if(t>=1):
     return("True")
    else:
     return("False")

#To perform the task of question
def task(a,b):
    r=list(range(a,b))
    q=[db(i) for i in range(a,b)]
    d={}
    for i in range(0,len(q)):
     d[r[i]]=do(q[i])
    print(d)

task(int(input("First number : ")),int(input("Second number : ")))


