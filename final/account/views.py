from django.shortcuts import render, redirect
# Use built-in user register and authentication functionalities
from books.models import Book
from .forms import RegisterForm


# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            books = Book.objects.all()
            books_dict = {"book": books}
            return render(response, 'books/home.html', books_dict)
    else:
        form = RegisterForm()
        return render(response, 'account/register.html', {'title': "Create an account", "form": form})


def logout(request):
    if request.method == 'POST':
        return redirect('/accounts/logout')
    else:
        return render(request, 'account/logout.html', {'title': 'Deleting...'})