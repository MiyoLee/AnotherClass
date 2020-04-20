from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'firstApp/index.html')

def blogMain(request):
    return render(request, 'firstApp/blogMain.html')

def categoryselect(request):
    return render(request, 'firstApp/categoryselect.html')

