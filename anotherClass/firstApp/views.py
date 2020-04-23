from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.views import generic
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

def createclass(request):
    return render(request, 'firstApp/createclass.html')

def community(request):
    post_list = Post.objects.all()
    return render(request, 'firstApp/community.html', {
        'post_list': post_list, })

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'firstApp/post_detail.html', {
        'post': post, })

def createpost(request):

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('community')
    else:
        form = PostForm()
        return render(request, 'firstApp/createpost.html', {'form': form})

def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
        return redirect('post_detail', pk=pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'firstApp/update_post.html', {'form': form})

def delete_post(request,pk):
    post=get_object_or_404(Post,pk=pk)
    post.delete()
    return redirect('community')

def login(request):
    return render(request, 'firstApp/login.html')

