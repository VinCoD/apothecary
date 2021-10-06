from django.shortcuts import render
from .models import Parent


def index(request):
    return render(request, 'index.html')

def available_meds(request):
    return render(request, 'available_meds.html')

def parents(request):
    parents = Parent.objects.all()
    context = {'parents': parents}
    return render(request, 'parents.html', context)

def children(request, ida):
    parent = Parent.objects.get(id=ida)
    children = parent.child_set.order_by('-date_added')
    context = {'children': children, 'parent':parent}
    return render(request, 'children.html', context)