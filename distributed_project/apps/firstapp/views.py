from django.shortcuts import render, HttpResponse, redirect


#  #1: INDEX
def index(request):
    print("Index method.....")
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    print(" New method....")
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    print("create method ..... redirecting to index method")
    return redirect("/")

def show(request, id):
    print("show method")
    message = "placeholder to display blog number:  " + str(id)
    return HttpResponse(message)

def edit(request, id):
    message = "placeholder to edit blog " + str(id)
    return HttpResponse(message)

def destroy(request, id):
    print("redirecting from method destroy.... to index")
    return redirect('/')

