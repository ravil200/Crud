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
        return render(request, 'index.html', {'f': form})