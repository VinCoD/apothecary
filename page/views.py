from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def available_meds(request):
    return render(request, 'available_meds.html')