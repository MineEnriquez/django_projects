from django.shortcuts import render, HttpResponse
from .models import users2
from .models import Author
from .models import Book

def index(request):
    return HttpResponse("this is a response from index")

def displaydata(request):
    print("this is display data")
    context={
        "Users_Dataset": users2.objects.all()
    }
    return render(request, "howarts/index.html", context)

def newrecord(request):
    pass

