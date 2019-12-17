from django.shortcuts import render, HttpResponse, redirect
import datetime
import random
import string

def process_money(request):
    if request.method == "GET":
    	return render(request, "ninjita/index.html")

    if request.method == "POST":
        print("starting processing some money...")
        print(request)
        now = datetime.datetime.now().strftime('%Y/%m/%d %I:%M:%S %p')
        color = "green"

        min = int( request.POST['min'])
        max = int( request.POST['max'])
        print(f"...MIN:..{min}.....MAX....{max}......")

        x = random.randint(min, max)
        transaction = ""
        print(x)
        if x < 0:
            color = "red"
            transaction = "Lost"
        else:
            color = "green"
            transaction = "Earned"

        message = "<li style=\"color: " + color + ";\">" + transaction + \
            " " + str(x) + " golds for the farm (" + now + ")</li>"
        print(message)
        # Calculating total gold
        if 'total_gold' in request.session:
            request.session['total_gold'] = request.session['total_gold'] = request.session['total_gold'] + x
        else:
            request.session['total_gold'] = 0

        # updating the transactions list
        if 'activities' in request.session:
            request.session['activities'] = message + request.session['activities']
        else:
            request.session['activities'] = " "

        return render(request, "ninjita/index.html")

def something(request):
    return HttpResponse("Something happening here")

def reset(request):
    if 'total_gold' in request.session:
        print('clearing random number')
        request.session.clear()
        request.session['total_gold'] = 0
        request.session['activities'] =""
    return redirect("/")


