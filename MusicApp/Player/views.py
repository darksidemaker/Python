from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def get_song(request):
    name = request.POST.get('name')
    return render(request, 'index.html',{'name' : name})