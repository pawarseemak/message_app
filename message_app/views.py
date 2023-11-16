from django.shortcuts import render, HttpResponse, redirect
from .models import Msg

# Create your views here.
def create(request):
    if request.method=='POST':
       # print("request is:",request.method)
        n=request.POST['uname']
        mail=request.POST['uemail']
        mob=request.POST['umobile']
        msg=request.POST['msg']
        """ print(n)
        print(mail)
        print(mob)
        print(msg) """
        n=Msg.objects.create(name=n,email=mail,mobile=mob,msg=msg)
        n.save()
        return redirect('/dashboard')
        return HttpResponse("data inserted successfully")
    else:
       # print("reuest is:",request.method)
        return render (request,'create.html')

def dashboard(request):
    m=Msg.objects.all()
    #print(m)
    context={}
    context['data']=m
    #return HttpResponse("data fetched")
    return render(request, 'dashboard.html',context)

def delete(request,rid):
    n=Msg.objects.filter(id=rid)
    n.delete()
    return redirect('/dashboard')
    #return HttpResponse("id to be deleted: "+rid)

def edit(request,rid):
    if request.method=='POST':
        #submit form with new values
        n=request.POST['uname']
        mail=request.POST['uemail']
        mob=request.POST['umobile']
        msg=request.POST['msg']
        m=Msg.objects.filter(id=rid)
        m.update(name=n,email=mail,mobile=mob,msg=msg)
        #PRINT(M)
        return redirect('/dashboard')
    else:
        #display form with old data
        n=Msg.objects.get(id=rid)
        context={}
        context['data']=n
        return render(request, 'edit.html' ,context)
        #return HttpResponse("id to be edited: "+rid)