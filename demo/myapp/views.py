from django.shortcuts import render , HttpResponse, redirect
from .models import TodoItem
from .forms import Todofroms

# Create your views here.
def home(request):
    return render(request, "home.html")
    
def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})

def my_view(request):
    if request.method == 'POST':
        form = Todofroms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_data')
    else:
        form = Todofroms()
    return render(request, 'my_form.html', {'form': form})

def show_data(request):
    data = TodoItem.objects.all()
    return render(request, 'show_data.html', {'data': data})

# def delete_item(request, item_id):
#     item = TodoItem.objects.get(pk=item_id)
#     item.delete()
#     return redirect('show_data')