from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment, Class, Area
from .forms import PostForm, CommentForm
from .forms import CreateClass
from django.views import generic
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'firstApp/index.html')

def blogMain(request):
    classs = Class.objects.all()
    return render(request, 'firstApp/blogMain.html', {'classs':classs})

def categoryselect(request):
    sort = request.GET.get('sort', '')  # url의 쿼리스트링을 가져온다. 없는 경우 공백을 리턴한다

    if sort == 'best':
        classs = Class.objects.filter(category__name='best')  # 복수를 가져올수 있음
        return render(request, 'firstApp/categoryselect.html', {'classs':classs})

    elif sort == 'art':
        classs = Class.objects.filter(category__name='art')  # 복수를 가져올수 있음
        return render(request, 'firstApp/categoryselect.html', {'classs':classs})

    else:
        classs = Class.objects.all()
        return render(request, 'firstApp/categoryselect.html', {'classs':classs})


def product(request, class_id):
    class_detail = get_object_or_404(Class, pk=class_id)

    return render(request, 'firstApp/product.html', {'class_detail': class_detail})

def apply(request):
    return render(request, 'firstApp/apply.html')

def createclass(request):
    if request.method == 'POST':
        form = CreateClass(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            return redirect('index')
    else:
        form = CreateClass()
        return render(request, 'firstApp/createclass.html', {'form': form})


def community(request):
    if request.user is None:
        redirect('login')
    else:
        post_list = Post.objects.all()
        return render(request, 'firstApp/community.html', {
            'post_list': post_list, })

@login_required(login_url='/login/')
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = User.objects.get(username=request.user.get_username())
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
        post.views += 1
        post.save()
        return render(request, 'firstApp/post_detail.html', {
            'post': post, 'form': form})

@login_required(login_url='/login/')
def createpost(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = User.objects.get(username = request.user.get_username())
            post.save()
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
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('community')


def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)

def comment_update(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
        return redirect('post_detail', pk=comment.post.pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'firstApp/update_comment.html', {'form': form})

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/main')
        else:
            return render(request, 'firstApp/login.html', {'errer': 'username or password is incorrect'})
    else:
        return render(request, 'firstApp/login.html')

def signup(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                username=request.POST["username"], password=request.POST["password1"])
            auth.login(request, user)
            return redirect('/main')
        return render(request, 'firstApp/signup.html')
    return render(request, 'firstApp/signup.html')

def logout(request):
    auth.logout(request)
    return redirect('/main')

def createClass(request):
    return render(request, 'firstApp/createclass.html')

