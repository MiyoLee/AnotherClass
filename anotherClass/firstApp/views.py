from django.shortcuts import render
from .models import Post
# Create your views here.
def index(request):
    return render(request, 'firstApp/index.html')

def blogMain(request):
    return render(request, 'firstApp/blogMain.html')

def categoryselect(request):
    return render(request, 'firstApp/categoryselect.html')

def product(request):
    return render(request, 'firstApp/product.html')

def apply(request):
    return render(request, 'firstApp/apply.html')

def createpost(request):
    return render(request, 'firstApp/createpost.html')

def createclass(request):
    return render(request, 'firstApp/createclass.html')

def community(request):
    post_list = Post.objects.all()
    return render(request, 'firstApp/community.html', {'post_list': post_list, })
