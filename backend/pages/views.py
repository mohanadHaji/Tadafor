from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Message
from django.views.decorators.csrf import csrf_exempt
from itertools import chain
# Create your views here.
def index(request):
    return render(request,'index.html')
def staff(request):
    return render(request, 'staff.html')
@csrf_exempt
def psych(request,id=-1):
    if request.user.is_authenticated and request.user.id == 2:
        if request.method == 'POST' and request.POST.get('message') != '':
            t = Message(to_id=User.objects.get(id=id), from_id=request.user,message=request.POST.get('message'))
            t.save()
            return HttpResponse('succsses')
        m = Message.objects.filter(to_id=2).order_by('-id')
        users = {}
        for i in m:
            if users.get(i.from_id.username) == None:
                users[i.from_id.id] = User.objects.get(id=i.from_id.id)
                if id == -1:
                    return HttpResponseRedirect('/psych.html/'+ str(users[i.from_id.id].id)+"/")
        try:
            send=Message.objects.filter(from_id=users[id].id,to_id=2)
            rec=Message.objects.filter(from_id=2,to_id=users[id].id)
            messages=sorted(chain(rec, send),key=lambda instance: instance.id,reverse=True)
        except Exception:
            users = list(users.values())
            return HttpResponseRedirect('/psych.html/'+ str(users[0].id)+"/")
        users = list(users.values())
        return render(request,'psych.html',{"users":users, "messages":list(messages),"id":id})



    if request.user.is_authenticated:
        if request.method == 'POST' and request.POST.get('message') != '':
            t = Message(to_id=User.objects.get(id=2), from_id=request.user,message=request.POST.get('message'))
            t.save()
            return HttpResponse('succsses')
        send=Message.objects.filter(from_id=request.user.id,to_id=2)
        rec=Message.objects.filter(from_id=2,to_id=request.user.id)
        messages=sorted(chain(rec, send),key=lambda instance: instance.id,reverse=True)
        return render(request,'psych.html',{"messages":list(messages)})
    else:    
        return render(request,'psych.html')
    





@csrf_exempt
def rights(request,id=-1):
    if request.user.is_authenticated and request.user.id == 3:
        if request.method == 'POST' and request.POST.get('message') != '':
            t = Message(to_id=User.objects.get(id=id), from_id=request.user,message=request.POST.get('message'))
            t.save()
            return HttpResponse('succsses')
        m = Message.objects.filter(to_id=3).order_by('-id')
        users = {}
        for i in m:
            if users.get(i.from_id.username) == None:
                users[i.from_id.id] = User.objects.get(id=i.from_id.id)
                if id == -1:
                    return HttpResponseRedirect('/rights.html/'+ str(users[i.from_id.id].id)+"/")
        try:
            send=Message.objects.filter(from_id=users[id].id,to_id=3)
            rec=Message.objects.filter(from_id=3,to_id=users[id].id)
            messages=sorted(chain(rec, send),key=lambda instance: instance.id,reverse=True)
        except Exception:
            users = list(users.values())
            return HttpResponseRedirect('/rights.html/'+ str(users[0].id)+"/")
        users = list(users.values())
        return render(request,'rights.html',{"users":users, "messages":list(messages),"id":id})



    if request.user.is_authenticated:
        if request.method == 'POST' and request.POST.get('message') != '':
            t = Message(to_id=User.objects.get(id=3), from_id=request.user,message=request.POST.get('message'))
            t.save()
            return HttpResponse('succsses')
        send=Message.objects.filter(from_id=request.user.id,to_id=3)
        rec=Message.objects.filter(from_id=3,to_id=request.user.id)
        messages=sorted(chain(rec, send),key=lambda instance: instance.id,reverse=True)
        return render(request,'rights.html',{"messages":list(messages)})
    else:    
        return render(request,'rights.html')







@csrf_exempt
def feed(request,id=-1):
    if request.user.is_authenticated and request.user.id == 4:
        if request.method == 'POST' and request.POST.get('message') != '':
            t = Message(to_id=User.objects.get(id=id), from_id=request.user,message=request.POST.get('message'))
            t.save()
            return HttpResponse('succsses')
        m = Message.objects.filter(to_id=4).order_by('-id')
        users = {}
        for i in m:
            if users.get(i.from_id.username) == None:
                users[i.from_id.id] = User.objects.get(id=i.from_id.id)
                if id == -1:
                    return HttpResponseRedirect('/feed.html/'+ str(users[i.from_id.id].id)+"/")
        try:
            send=Message.objects.filter(from_id=users[id].id,to_id=4)
            rec=Message.objects.filter(from_id=4,to_id=users[id].id)
            messages=sorted(chain(rec, send),key=lambda instance: instance.id,reverse=True)
        except Exception:
            users = list(users.values())
            return HttpResponseRedirect('/feed.html/'+ str(users[0].id)+"/")
        users = list(users.values())
        return render(request,'feed.html',{"users":users, "messages":list(messages),"id":id})



    if request.user.is_authenticated:
        if request.method == 'POST' and request.POST.get('message') != '':
            t = Message(to_id=User.objects.get(id=4), from_id=request.user,message=request.POST.get('message'))
            t.save()
            return HttpResponse('succsses')
        send=Message.objects.filter(from_id=request.user.id,to_id=4)
        rec=Message.objects.filter(from_id=4,to_id=request.user.id)
        messages=sorted(chain(rec, send),key=lambda instance: instance.id,reverse=True)
        return render(request,'feed.html',{"messages":list(messages)})
    else:    
        return render(request,'feed.html')

def callus(request):
    return render(request,'callus.html')

def others(request):
    return render(request,'others.html')

def register(request):
    if request.method == 'POST':
        if request.POST.get('name') == '':
            nameInfo="الرجاء ادخال اسم"
            return render(request,'register.html',{"nameInfo":nameInfo})
        elif request.POST.get('password')=='':
            passInfo="الرجاء ادخال كلمة سر"
            return render(request,'register.html',{"passInfo":passInfo})
        elif request.POST.get('confirmPassword')=='':
            confInfo="الرجاء تاكيد كلمة سر"
            return render(request,'register.html',{"confInfo":confInfo})
        if request.POST.get('password') != request.POST.get('confirmPassword'):
            passInfo="تاكيد كلمة السر خاطئة"
            confInfo="تاكيد كلمة السر حاظئ"
            return render(request,'register.html',{"passInfo":passInfo,"confInfo":confInfo})

        try:
            user = User.objects.create_user(username=request.POST.get('name'), password=request.POST.get('password'))
            return HttpResponseRedirect('/login')
            
        except Exception:
            nameInfo="الاسم مستخدم من قبل مستخدم اخر"
            return render(request,'register.html',{"nameInfo":nameInfo})

        
    return render(request,'register.html',{})

