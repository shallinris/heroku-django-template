from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Entry
from django import forms
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .forms import form1



# Create your views here.
@login_required
def index(request):
    post_list = Entry.objects.order_by("-date")
    context = {'post_list':post_list}
    #save list of objects from db in variable Entry.objects.orderby("-date")
    #add said variable to dictionary called context context={'post_list':post_list}
    #put that as the 3rd parameter of the the render function
    #THEN...write the code in the template to loop through 'post_list'.
    return render(request, 'billboard/index.html', context)

@login_required
def get_new_entry(request):
    print("valid")
    title = request.POST.get('title')
    message = request.POST.get('message')
    author = request.POST.get('author')
    e = Entry(author=author, title=title, text=message)
    e.save()
    return HttpResponseRedirect('/billboard')
    # post_list = Entry.objects.order_by("-date")
    # context = {'post_list': post_list}
    # return render(request, 'billboard/index.html',context)

@login_required
def delete_entry(request):
    del_id = request.POST.get('delete')
    obj_del = Entry.objects.get(pk=del_id)
    obj_del.delete()
    return HttpResponseRedirect('/billboard')

def signupform(request):
    f=form1()
    return render(request,'billboard/signup.html',{'form':f})

def newUserCreated(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        new_user = User.objects.create_user(username, email, password)
        new_user.save()
        return HttpResponseRedirect('/billboard/')


