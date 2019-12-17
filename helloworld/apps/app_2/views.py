from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse
# Create your views here.

# url(r'^$', views.index),


def forma(request):
    print("Hello from the index view.index   function")
    context = {
        "name": "Noelle",
        "favorite_color": "turquoise",
        "pets": ["Bruce", "Fitz", "Georgie"]
    }
    return render(request, 'app_2/index.html', context)

    # url(r'hello$', views.sayhello),


def sayhello(request):
    print("Say hello.....")
    return HttpResponse("This is the equivalent of @app.route('/sayhello')")

    # url(r'bye$', views.saygoodbye),


def saygoodbye(request):
    print("Say good bye")
    return HttpResponse("this is the equivalent of @app.route('/saygoodbye')")


def one_method(request):
    print("one method.....")
    return HttpResponse("one method sample")


def another_method(request, my_val):
    print("aanother method with params")
    return HttpResponse("another method with parameters now")

# would match localhost:8000/bears/pooh/poke
# url(r'^bears/(?P<name>\w+)/poke$', views.yet_another),


def yet_another(request, name):
    print("yet another one with two parameters")
    return HttpResponse(" sample with two parametersthis is equivalent to  @app.route('/yet_another/<name>/poke') ?????")

# would match localhost:8000/17/brown
# url(r'^(?P<id>[0-9]+)/(?P<color>\w+)$', views.one_more),


def one_more(request, id, color):
    print("yei one more with params: id and color")
    return HttpResponse(" this is the equivalent of @app.route('/one_more/<int:id>/<color>') ?????")
