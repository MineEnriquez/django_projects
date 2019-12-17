from django.shortcuts import render, HttpResponse
import datetime

def index(request):
    print("Hello from the index view.index   function")
    d = datetime.datetime.now().strftime("%B %d, %Y")
    t = datetime.datetime.now().strftime("%I:%M %p")
    context = {
        "date": str(d),
        "time": str(t),
    }
    return render(request, "singleapp/index.html", context)
