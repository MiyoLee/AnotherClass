from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment, Class, Category, ClassQna
from .forms import PostForm, CommentForm, QuestionForm, SignupForm
from .forms import CreateClass
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView
from django.contrib.auth.hashers import check_password
from django.urls.base import reverse

# Create your views here.
def index(request):
    return render(request, 'firstApp/index.html')

def mypage(request):
    return render(request, 'firstApp/mypage.html')

def blogMain(request):
    classs = Class.objects.all()
    return render(request, 'firstApp/blogMain.html', {'classs':classs})

def categoryselect(request):
    sort = request.GET.get('sort', '')  # url의 쿼리스트링을 가져온다. 없는 경우 공백을 리턴한다

    if sort == 'best':
        classs = Class.objects.filter(category__name='베스트')  # 복수를 가져올수 있음
        return render(request, 'firstApp/categoryselect.html', {'classs': classs})

    elif sort == 'art':
        classs = Class.objects.filter(category__name='미술, 공예')  # 복수를 가져올수 있음
        return render(request, 'firstApp/categoryselect.html', {'classs': classs})

    elif sort == 'music':
        classs = Class.objects.filter(category__name='음악, 댄스')  # 복수를 가져올수 있음
        return render(request, 'firstApp/categoryselect.html', {'classs': classs})

    elif sort == 'career':
        classs = Class.objects.filter(category__name='커리어')  # 복수를 가져올수 있음
        return render(request, 'firstApp/categoryselect.html', {'classs': classs})

    elif sort == 'language':
        classs = Class.objects.filter(category__name='언어')  # 복수를 가져올수 있음
        return render(request, 'firstApp/categoryselect.html', {'classs': classs})
    else:
        classs = Class.objects.all()
        return render(request, 'firstApp/categoryselect.html', {'classs': classs})




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
        cate_list = Category.objects.all()
        post_list = Post.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(post_list, 10)
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        return render(request, 'firstApp/community.html', {
            'posts': posts, 'cate_list': cate_list })


def post_category(request, pk):
    cate_list = Category.objects.all()
    post_list = Post.objects.filter(category=pk)
    page = request.GET.get('page', 1)
    paginator = Paginator(post_list, 10)
    try:
           posts = paginator.page(page)
    except PageNotAnInteger:
           posts = paginator.page(1)
    except EmptyPage:
           posts = paginator.page(paginator.num_pages)
    return render(request, 'firstApp/community.html', {
        'posts': posts, 'cate_list': cate_list})

@login_required(login_url='/login/')
def myPost(request):
    cate_list = Category.objects.all()
    post_list = Post.objects.filter(author=request.user)
    page = request.GET.get('page', 1)
    paginator = Paginator(post_list, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'firstApp/community.html', {
       'posts': posts, 'cate_list': cate_list})

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


def product(request, class_id):
    class_detail = get_object_or_404(Class, pk=class_id)
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.inClass = class_detail
            question.save()
            return HttpResponseRedirect("/product/{}".format(class_id))
    else:
        form = QuestionForm()
        class_detail.save()
        return render(request, 'firstApp/product.html', {
            'class_detail': class_detail, 'form': form})


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
    context= {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/main')
        else:
            context.update({'error':"아이디나 비밀번호를 확인하세요."})
            return render(request, 'firstApp/login.html', context)
    else:
        return render(request, 'firstApp/login.html')

def signup(request):
    if request.method == "GET":
        return render(request, 'firstApp/signup.html', {'f':SignupForm()} )
    
    elif request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password']  == form.cleaned_data['password_check']:
                new_user = User.objects.create_user(form.cleaned_data['username'],form.cleaned_data['email'],form.cleaned_data['password'])
                new_user.last_name = form.cleaned_data['last_name']
                new_user.first_name = form.cleaned_data['first_name']
                new_user.save()
                return redirect('/main')      
            else:
                return render(request, 'firstApp/signup.html',{'f':form, 'error':'비밀번호와 비밀번호 확인이 다릅니다.'})

        else:
            return render(request, 'firstApp/signup.html',{'f':form})

def logout(request):
    auth.logout(request)
    return redirect('/main')

def change_pw(request):
    context= {}
    if request.method == "POST":
        current_password = request.POST.get("origin_password")
        user = request.user
        if check_password(current_password,user.password):
            new_password = request.POST.get("password1")
            password_confirm = request.POST.get("password2")
            if new_password == password_confirm:
                user.set_password(new_password)
                user.save()
                auth.login(request,user)
                return redirect('/main')
            else:
                context.update({'error':"새 비밀번호를 다시 확인해주세요."})
        else:
            context.update({'error':"현재 비밀번호가 일치하지 않습니다."})

    return render(request, "firstApp/change_pw.html",context)
