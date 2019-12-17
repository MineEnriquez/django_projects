from django.shortcuts import render, HttpResponse, redirect
from .models import books, authors
# Create your views here.

def index(request):
        context = {
            "all_books" : books.objects.all()
        }
        return render(request, "books_authors_app/index.html", context)

def add(request):
    books.objects.create(title=request.POST['title'], desc=request.POST['desc'])
    return redirect('/')


def showbook(request, book_id):
    the_book = books.objects.get(id = book_id)
    the_authors = authors.objects.all()
    context = {
        "book_info" : the_book,
        "authors_info" : authors.objects.filter(books = the_book),
        "all_authors" : the_authors
    }
    return render(request, "books_authors_app/showbook.html", context)

def addauthor(request):
    the_book = books.objects.get(id = request.POST['book_id'])
    the_author = authors.objects.get(id = request.POST['author_id'])
    the_author.books.add(the_book)
    origin = "/books/" + str(request.POST['book_id'])
    return redirect(origin)

def authorspage(request):
    if request.method == "GET":
        print(request.GET)

    if request.method == "POST":
        print(request.POST.Name)
    all_authors = authors.objects.all()
    context = {
        "all_authors" : all_authors
    }
    return render(request, "books_authors_app/authors.html", context)

def createauthor(request):
    authors.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], notes=request.POST['notes'])
    print("the author has been crdated")
    return redirect('/authors')

def showauthor(request, author_id):
    the_author = authors.objects.get(id = author_id)
    the_books = the_author.books.all()
    all_books = books.objects.all()
    context = {
        "books_info" : the_books,
        "author_info" : the_author,
        "all_books" : all_books
    }
    return render(request, "books_authors_app/showauthors.html", context)

def addbooktoauthor(request):
    the_book = books.objects.get(id = request.POST['book_id'])
    the_author = authors.objects.get(id = request.POST['author_id'])
    the_author.books.add(the_book)
    origin = "/authors/" + str(request.POST['author_id'])
    return redirect(origin)