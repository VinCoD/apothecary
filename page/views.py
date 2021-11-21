from django.shortcuts import redirect, render

from page.forms import ParentForm
from .models import Parent


def index(request):
    return render(request, 'page/index.html')

def available_meds(request):
    return render(request, 'page/available_meds.html')

def parents(request):
    parents = Parent.objects.all()
    context = {'parents': parents}
    return render(request, 'page/parents.html', context)

def children(request, ida):
    parent = Parent.objects.get(id=ida)
    children = parent.child_set.order_by('-date_added')
    context = {'children': children, 'parent':parent}
    return render(request, 'page/children.html', context)

def new_parent(request):
    if request.method != 'POST':
        form = ParentForm()
    else:
        form = ParentForm(data=request.POST)
        if form.is_valid:
            form.save()
            return redirect('page:parents')
    
    context = {'form': form}
    return render(request, 'page/new_parent.html', context)
    