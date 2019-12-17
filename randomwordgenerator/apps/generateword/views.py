from django.shortcuts import render, HttpResponse, redirect
import datetime, random, string

def index(request):
    print("Hello from the Generate    function")
    r = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(20)])
    print(r)
    counter = -1

    if 'total' in request.session:
        counter = int(request.session['total'])
        print(request.session['total'])
    else:
        request.session['total']=0
  
    counter+=1
    request.session['total'] = counter

    if counter > 0:
        request.session['random_word'] = r
    return render(request, "generateword/index.html")

def reset(request):
    request.session['total'] = -1
    request.session['random_word'] = " "
    render(request, "generateword/index.html")
    return redirect("/")