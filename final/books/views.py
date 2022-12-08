from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import bookForm
from .models import Book


# Create your views here.
def hello(request):
    books = Book.objects.all()
    books_dict = {"book": books, "user": request.user}
    return render(request, "books/home.html", books_dict)


def displayById(request, id):
    b = Book.objects.get(id=id)
    return render(request, "books/byID.html", {"title": b.title, "item": b})


@login_required
def addBook(request):
    # Create movie form object
    form = bookForm()
    # When form submitted
    if request.method == 'POST':
        u = User.objects.get(id=request.POST.get('user'))
        # Create movie object from form
        Book.objects.create(
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            year=request.POST.get('year'),
            rating=request.POST.get('rating'),
            author=request.POST.get('author'),
            posted_by=u
        )
        # Redirect to homepage
        return redirect('/')

    context = {'form': form, "title": "Add Book"}
    return render(request, 'books/addBook.html', context)


@login_required
def editBook(request, id):
    book = Book.objects.get(id=id)
    form = bookForm(instance=book)
    # When form submitted get values
    if request.method == 'POST':
        if request.user == book.posted_by:
            # Update model based on form values
            title = request.POST.get('title'),
            description = request.POST.get('description'),
            year = request.POST.get('year'),
            rating = request.POST.get('rating'),
            author = request.POST.get('author')
            # Save model in db
            book.save()
            # Redirect to hom
            return redirect('/')
        else:
            return HttpResponse("<h2>You are not the creator of the review...</h2>")

    # Return and render movie form
    context = {'form': form, 'b': book, "title": "Update Book"}
    return render(request, 'books/editBook.html', context)


@login_required
def deleteBook(request, id):
    b = Book.objects.get(id=id)
    if request.method == 'POST':
        if request.user == b.posted_by:
            b.delete()
            return redirect('/')
        else:
            return HttpResponse("<h2>You are not the creator of the review...</h2>")
    else:
        return render(request, 'books/deleteBook.html', {'b': b, 'title': 'Deleting...'})
