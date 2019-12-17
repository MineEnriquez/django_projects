from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("this is a response from index")
