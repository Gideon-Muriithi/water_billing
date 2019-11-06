from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *
from .models import*

def landingpage(request):

    title = 'Landing'

    return render(request, 'landing_page.html', {'title': title})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'user/registration/register.html', {'form':form})

@login_required
def home(request):
    return render(request, 'home.html')


@login_required
def account_details(request):
    profile = request.user
    details = Detail.get_account(profile.id)
    return render(request, 'account/details.html', {'details': details})

@login_required
def account_status(request):
    profile = request.user
    statuses = Status.get_account(profile.id)
    return render(request, 'account/account_status.html', {'statuses': statuses})


@login_required
def payments(request):
    profile = request.user
    payments = Payment.get_account(profile.id)
    messages.success(request, f'Your payment has been received successfully!')
    return render(request, 'account/payments.html', {'payments': payments})

@login_required
def bills(request):
    profile = request.user
    bills = Bill.get_account(profile.id)
    messages.success(request, f'Water consumption units confirmed successfully! The following is this month\'s bill.')
    return render(request, 'account/bills.html', {'bills': bills })


@login_required
def units(request):
    profile = request.user
    units = Unit.get_account(profile.id)
    return render(request, 'account/units.html', {'units': units })

def units_refute(request):
    return render(request, 'account/units_refute.html')