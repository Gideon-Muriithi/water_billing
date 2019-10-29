from django.shortcuts import render

def landingpage(request):
    title = 'Landing'

    return render(request, 'landing_page.html', {'title': title})
