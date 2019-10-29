from django.shortcuts import render, redirect
from .forms import *

def landingpage(request):
    title = 'Landing'

    return render(request, 'landing_page.html', {'title': title})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_date.get('username')
            # return redirect()

    else:
        form = UserRegisterForm()
    return render(request, 'user/registration/register.html', {'form':form})
