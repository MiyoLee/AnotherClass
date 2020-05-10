from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment, Class, Category, ClassQna
from .forms import PostForm, CommentForm, QuestionForm, SignupForm, CreateClass, ApplyForm
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView
from django.contrib.auth.hashers import check_password
from django.urls.base import reverse
from django.http.response import HttpResponseNotAllowed

# Create your views here.
def index(request):
    return render(request, 'firstApp/index.html')

def mypage(request):
    return render(request, 'firstApp/mypage.html')

def blogMain(request):
    classs = Class.objects.all()
    return render(request, 'firstApp/blogMain.html', {'classs':classs})


@login_required(login_url='/login/')
def myClass(request):
    classs = Class.objects.filter(author=request.user)
    return render(request, 'firstApp/classlist.html', {'classs':classs})

@login_required(login_url='/login/')
def myApply(request):
    classs = Class.objects.filter(author=request.user)
    return render(request, 'firstApp/applylist.html', {'classs':classs})
       
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



@login_required(login_url='/login/')
def apply(request, class_id):
    class_detail = get_object_or_404(Class, pk=class_id)
    if request.method == 'POST':
        form = ApplyForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = User.objects.get(username = request.user.get_username())
            post.save()
            return redirect("/product/{}".format(class_id))
        else:
            return render(request, 'firstApp/apply.html',{'form': form, 'alert_flag': True})
    else:
        form = ApplyForm()
        return render(request, 'firstApp/apply.html', {'form': form})

@login_required(login_url='/login/')
def createclass(request):
    if request.method == 'POST':
        form = CreateClass(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = User.objects.get(username = request.user.get_username())
            post.save()
            return redirect('main')
        else:
            return render(request, 'firstApp/createclass.html',{'form': form, 'alert_flag': True})
    else:
        form = CreateClass()
        return render(request, 'firstApp/createclass.html', {'form': form})

def update_class(request, class_id):
    class_detail = get_object_or_404(Class, pk=class_id)
    if request.method == 'POST':
        form = CreateClass(request.POST, request.FILES, instance=class_detail)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = User.objects.get(username = request.user.get_username())
            post.save()
            return redirect("/product/{}".format(class_id))
        else:
            return render(request, 'firstApp/update_class.html',{'form': form, 'alert_flag': True})
    else:
        form = CreateClass(instance=class_detail)
        return render(request, 'firstApp/update_class.html', {'form': form})

def community(request):
    if request.user is None:
        redirect('login')
    else:
        cateId = request.GET.get('cateId', '')  # url의 쿼리스트링을 가져온다. 없는 경우 공백을 리턴한다
        cate_list = Category.objects.all()
        if cateId == '':
            post_list = Post.objects.all()
            cateName = '전체 글'
        else:
            post_list = Post.objects.filter(category=cateId)
            cateName = get_object_or_404(Category, pk=cateId).name
        page = request.GET.get('page', 1)
        paginator = Paginator(post_list, 10)
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        return render(request, 'firstApp/community.html', {
            'posts': posts, 'cate_list': cate_list, 'cateName': cateName, 'cateId':cateId})




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
    page = request.GET.get('page', 1)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = User.objects.get(username=request.user.get_username())
            comment.save()
            return render(request, 'firstApp/post_detail.html', {
                'post': post, 'form': CommentForm(), 'page': page})
    else:
        form = CommentForm()
        post.views += 1
        post.save()
        return render(request, 'firstApp/post_detail.html', {
            'post': post, 'form': form, 'page': page})


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
    page = request.GET.get('page', 1)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
        return redirect('post_detail', pk=pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'firstApp/update_post.html', {'form': form})

def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('community')


def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)

def comment_update(request, pk):
    my_comment = get_object_or_404(Comment, pk=pk)
    page = request.GET.get('page', 1)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=my_comment)
        if form.is_valid():
            form.save()
        return render(request, 'firstApp/post_detail.html', {
                'post': my_comment.post, 'form': CommentForm(), 'page': page})
    else:
        form = CommentForm(instance=my_comment)
    return render(request, 'firstApp/update_comment.html', {'my_comment': my_comment, 'post': my_comment.post, 'form': form, 'page': page})


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/main')
        else:
            return render(request, 'firstApp/login.html', {'alert_flag': True})
    else:
        return render(request, 'firstApp/login.html')

def signup(request):
    if request.method == "GET":
        return render(request, 'firstApp/signup.html', {'f':SignupForm()} )
    elif request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password']  == form.cleaned_data['비밀번호_확인']:
                new_user = User.objects.create_user(form.cleaned_data['username'],form.cleaned_data['email'],form.cleaned_data['password'])
                new_user.last_name = form.cleaned_data['last_name']
                new_user.first_name = form.cleaned_data['first_name']
                new_user.save()
                return redirect('/main')
            else:
                return render(request, 'firstApp/signup.html',{'f':form, 'alert_flag1': True})
        else:
            return render(request, 'firstApp/signup.html',{'f':form, 'alert_flag2': True})

def logout(request):
    auth.logout(request)
    return redirect('/main')

def change_pw(request):
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
                return render(request, 'firstApp/change_pw.html', {'alert_flag1': True})
        else:
            return render(request, 'firstApp/change_pw.html', {'alert_flag2': True})

    return render(request, "firstApp/change_pw.html")
