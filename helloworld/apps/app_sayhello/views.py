from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse
def index(request):
    print(" Hello world in the console.. ......................")
    return HttpResponse("this is the equivalent of @app.route('/')!")