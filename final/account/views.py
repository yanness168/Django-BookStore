from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
# Use built-in user register and authentication functionalities
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm


# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            form.save()
            user = User.objects.get(username=username)
            try:
                login(request, user)
                return redirect('/')
            except:
                pass
        else:
            return render(request, 'account/register.html', {'title': "Create an account", "form": form})
    else:
        form = RegisterForm()
        return render(request, 'account/register.html', {'title': "Create an account", "form": form})


@login_required
def logout(request):
    if request.method == 'POST':
        return redirect('/accounts/logout')
    else:
        user = request.user
        return render(request, 'account/logout.html', {'title': 'Deleting...', 'user': user})
