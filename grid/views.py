from django.shortcuts import render, redirect
from .models import Employer
from .forms import EmployerForm


def addnew(request):
    if request.method == 'POST':
        form = EmployerForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                pass
    else:
        form = EmployerForm()
        return render(request, 'index.html', {'form': form})

def index(request):
    employers = Employer.objects.all()
    return render(request, 'show.html', {'employers':employers})


def edit(request, id):
    employer = Employer.objects.get(id=id)
    context = {'employer': employer}
    return render(request, 'edit.html', context)

def update(request, id):
    employer = Employer.objects.get(id=id)
    form = EmployerForm(request.POST, instance=employer)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'employer':employer})

def delete(request, id):
    employer = Employer.objects.get(id=id)
    employer.delete()
    return redirect('/')

def homepage(request):
    if request.method == '/homepage':
        form = EmployerForm(request.homepage)
        if form.is_valid():
            try:
                form.save()
                return redirect('/homepage')
            except:
                pass
    else:
        form = EmployerForm()
        return render(request, 'index.html', {'form': form})
