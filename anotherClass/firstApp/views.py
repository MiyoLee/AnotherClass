from django.shortcuts import render, get_object_or_404, redirect
from .models import Photo, Post, Comment, CComment, Bullet, Class, Category, ClassQna, Apply, ClassDate, Certificate, Education, ClassAnswer, ClassReview, Area, Level, Profile
from .forms import ClassSale, PostForm, CommentForm, CCommentForm, QuestionForm, SignupForm, CreateClass, ReviewForm, ApplyForm, AddTime, CertificateForm, EducationForm, AnswerForm, CheckPasswordForm, ProfileForm, UserForm
from django.contrib.auth.models import User
from django.forms import modelformset_factory
from django.template import RequestContext
from django.utils import timezone
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.views.generic import FormView
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView
from django.contrib.auth.hashers import check_password
from django.urls.base import reverse
from django.http.response import HttpResponseNotAllowed
from django.db.models import Q
from annoying.functions import get_object_or_None
from django.shortcuts import render
from .filters import ClassFilter
'''
class ClassListView(ListView):
    model = Class
    template_name = 'firstApp/class_search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ClassFilter(self.request.GET, queryset=self.get_queryset())
        return context
'''
def index(request):
    return render(request, 'firstApp/index.html')

def mypage(request):
    return render(request, 'firstApp/mypage.html')

def blogMain(request):
    classs = Class.objects.filter(on_permission=True)
    best = Class.objects.filter(on_permission=True).order_by('-like_count')[:10]
    slide = Class.objects.filter(on_permission=True, category__name='미술, 공예')
    return render(request, 'firstApp/blogMain.html', {'classs': classs, 'slide': slide, 'best': best})

def intro_createclass(request):
    return render(request, 'firstApp/intro_createclass.html')

@login_required(login_url='/login/')
def myClass(request):
    classs = Class.objects.filter(author=request.user)
    return render(request, 'firstApp/classlist.html', {'classs':classs})

@login_required(login_url='/login/')
def myApply(request):
    applys = Apply.objects.filter(author=request.user)
    now = timezone.now()
    return render(request, 'firstApp/applylist.html', {'applys':applys, 'now':now})

def cancelApply(request, pk):
    apply = get_object_or_404(Apply, pk=pk)
    apply.delete()
    profile = request.user.profile
    profile.sybermoney = profile.sybermoney + int(apply.inClass.sale_price)
    profile.save()
    return redirect('myApply')

@login_required(login_url='/login/')
def mylike(request):
    classs = Class.objects.filter(on_permission=True, like_user=request.user)
    return render(request, 'firstApp/mylike.html', {'classs':classs})

@login_required(login_url='/login/')
def sybermoney(request):
    applys = Apply.objects.filter(author=request.user)
    profiles = Profile.objects.filter(user=request.user)
    return render(request, 'firstApp/sybermoney.html', {'applys':applys, 'profiles':profiles})

@login_required(login_url='/login/')
def member(request):
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('mypage')
        else:
            return render(request, 'firstApp/member_info_management.html', {'alert_flag': True, 'user_form': user_form, 'profile_form': profile_form})
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        return render(request, 'firstApp/member_info_management.html', {'user_form': user_form, 'profile_form': profile_form})

def class_align(request):
    classs = Class.objects.filter(on_permission=True)
    areas = Area.objects.all()
    categorys = Category.objects.all()
    levels = Level.objects.all()
    r = request.GET.get('r', '') #정렬
    if r == '1':
        classs = Class.objects.filter(on_permission=True).order_by('price')
    elif r == '2':
        classs = Class.objects.filter(on_permission=True).order_by('-price')
    else:
        classs = Class.objects.filter(on_permission=True)
    return render(request, 'firstApp/class_search.html', {'r': r, 'classs': classs,
    'levels' : levels, 'areas': areas, 'categorys' : categorys})


def is_valid_queryparam(param):
    return param != '' and param is not None
def class_search(request):
    #filter 기능...건들지마..
    price1 = request.GET.get('price1', '')
    price2 = request.GET.get('price2', '')
    class_list = Class.objects.filter(on_permission=True)
    if is_valid_queryparam(price1):
        class_list = class_list.filter(sale_price__gte=price1)
    if is_valid_queryparam(price2):
        class_list = class_list.filter(sale_price__lte=price2)

    class_filter = ClassFilter(request.GET, queryset=class_list)

    #classs = Class.objects.filter(on_permission=True).order_by('-like_count')

    return render(request, 'firstApp/class_search.html', {'filter': class_filter, 'price1': price1, 'price2': price2})

@login_required(login_url='/login/')
def apply(request, class_id):
    date_id = request.GET.get('date', '')
    date = get_object_or_404(ClassDate, pk=date_id)
    class_detail = get_object_or_404(Class, pk=class_id)
    if request.method == "POST":
        form = ApplyForm(request.POST)
        if form.is_valid():
            apply = form.save(commit=False)
            apply.author = User.objects.get(username=request.user.get_username())
            apply.inClass = class_detail
            apply.date = date
            apply.save()
            return HttpResponseRedirect("/product/{}".format(class_id) + '/apply/apply_complete')
        else:
            return render(request, 'firstApp/apply.html', {'alert_flag': True, 'class_detail': class_detail, 'form': form})
    else:
        form = ApplyForm()
        return render(request, 'firstApp/apply.html', {'class_detail': class_detail, 'form': form, 'date': date})

def review(request, class_id):
    class_detail = get_object_or_404(Class, pk=class_id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.inClass = class_detail
            review.save()
            return HttpResponseRedirect("/product/{}".format(class_id))
        else:
            return render(request, 'firstApp/create_review.html', {'alert_flag': True, 'class_detail': class_detail, 'form': form})
    else:
        form = ReviewForm()
        return render(request, 'firstApp/create_review.html', {'class_detail': class_detail, 'form': form})

def applicant(request, class_id):
    class_detail = get_object_or_404(Class, pk=class_id)
    return render(request, 'firstApp/applicant.html', {'class_detail': class_detail})

@login_required(login_url='/login/')
def createclass(request):
    if request.method == 'POST':
        form = CreateClass(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.price = post.price.replace(',', '')
            post.sale_price = post.price
            post.author = User.objects.get(username = request.user.get_username())
            post.save()
            for img in request.FILES.getlist('imgs'):
                photo = Photo()
                photo.post = post
                photo.image = img
                photo.save()
            return redirect('/createclass/'+str(post.id)+'/addTutor/')
        else:
            return render(request, 'firstApp/createclass.html')
    else:
        form = CreateClass()
        return render(request, 'firstApp/createclass.html', {'form': form})


def product_remove(request, pk):
    product = get_object_or_404(Class, pk=pk)
    product.delete()
    return redirect('myClass')

def time_remove(request, pk):
    time = get_object_or_404(ClassDate, pk=pk)
    time.delete()
    return redirect('addTime', class_id=time.inClass.pk)

def certi_remove(request, pk):
    certi = get_object_or_404(Certificate, pk=pk)
    certi.delete()
    return redirect('addTutor', class_id=certi.inClass.pk)

def edu_remove(request, pk):
    edu = get_object_or_404(Education, pk=pk)
    edu.delete()
    return redirect('addTutor', class_id=edu.inClass.pk)

def addTutor(request, class_id):
    class_detail = get_object_or_404(Class, pk=class_id)
    if request.method == "POST":
        form1 = CertificateForm(request.POST)
        form2 = EducationForm(request.POST)
        if form1.is_valid():
            certi = form1.save(commit=False)
            certi.inClass = class_detail
            certi.save()
            return HttpResponseRedirect("/createclass/{}/addTutor".format(class_id))
        if form2.is_valid():
            edu = form2.save(commit=False)
            edu.inClass = class_detail
            edu.save()
            return HttpResponseRedirect("/createclass/{}/addTutor".format(class_id))
    else:
        form1 = CertificateForm()
        form2 = EducationForm()
        class_detail.save()
        return render(request, 'firstApp/addTutor.html', {
            'class_detail': class_detail, 'form1': form1, 'form2': form2})

def create_complete(request, class_id):
    class_detail = get_object_or_404(Class, pk=class_id)
    return render(request, 'firstApp/create_complete.html', {'class_detail': class_detail})

def apply_complete(request, class_id):
    profiles = Profile.objects.filter(user=request.user)
    class_detail = get_object_or_404(Class, pk=class_id)
    profile = request.user.profile
    profile.sybermoney = profile.sybermoney - int(class_detail.sale_price)
    profile.save()
    return render(request, 'firstApp/apply_complete.html', {'class_detail': class_detail, 'profiles':profiles})

def update_answer(request, pk):
    answer = get_object_or_404(ClassAnswer, pk=pk)
    parent_question = get_object_or_404(ClassQna, pk=answer.inQuestion.pk)
    class_detail = get_object_or_404(Class, pk=answer.inClass.pk)

    if request.method == 'POST':
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.inClass = class_detail
            answer.inQuestion = parent_question
            answer.author = User.objects.get(username=request.user.get_username())
            answer.save()
        return HttpResponseRedirect("/product/{}/#qna".format(class_detail.id))

    else:
        form = AnswerForm(instance=answer)
        parent_question.save()
    return render(request, 'firstApp/update_answer.html',
                  {'class_detail': class_detail, 'form': form, 'parent_question': parent_question}
                  )

def create_answer(request, pk):
    parent_question = get_object_or_404(ClassQna, pk=pk)
    class_detail = get_object_or_404(Class, pk=parent_question.inClass.pk)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.inClass = class_detail
            answer.inQuestion = parent_question
            answer.author = User.objects.get(username=request.user.get_username())
            answer.save()
        return HttpResponseRedirect("/product/{}/#qna".format(class_detail.id))

    else:
        form = AnswerForm()
    return render(request, 'firstApp/create_answer.html',
                  {'class_detail': class_detail, 'form': form, 'parent_question': parent_question}
                  )

@login_required(login_url='/login/')
def like(request, class_id):
    class_detail = get_object_or_404(Class, pk=class_id)
    if request.user in class_detail.like_user.all():
        class_detail.like_user.remove(request.user)
        class_detail.like_count -=1
        class_detail.save()
    else:
        class_detail.like_user.add(request.user)
        class_detail.like_count +=1
        class_detail.save()
    return HttpResponseRedirect("/product/{}".format(class_id))




def product(request, class_id):
    class_detail = get_object_or_404(Class, pk=class_id)
    heart = 0
    if request.user in class_detail.like_user.all():
        heart = 1

    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.inClass = class_detail
            question.author = User.objects.get(username=request.user.get_username())
            question.save()
            return HttpResponseRedirect("/product/{}".format(class_id))
    else:
        form = QuestionForm()
        class_detail.save()
        return render(request, 'firstApp/product.html', {
            'class_detail': class_detail, 'heart': heart, 'form': form})

def addTime(request, class_id):
    class_detail = get_object_or_404(Class, pk=class_id)
    if request.method == "POST":
        form = AddTime(request.POST)
        if form.is_valid():
            time = form.save(commit=False)
            time.inClass = class_detail
            time.save()
            return HttpResponseRedirect("/createclass/{}/addTime".format(class_id))
    else:
        form = AddTime()
        class_detail.save()
        return render(request, 'firstApp/addTime.html', {
            'class_detail': class_detail, 'form': form})



def classSale(request, class_id):
    class_detail = get_object_or_404(Class, pk=class_id)
    if request.method == 'POST':
        form = ClassSale(request.POST, instance=class_detail)
        if form.is_valid():
            post = form.save(commit=False)
            post.sale_price = post.sale_price.replace(',', '')
            if post.sale_price == None :
                post.sale_price = class_detail.price
            post.save()
            return HttpResponseRedirect("/product/{}".format(class_id))
        else:
            return render(request, 'firstApp/classSale.html', {'form': form, 'alert_flag': True})
    else:
        form = ClassSale(instance=class_detail)
        return render(request, 'firstApp/classSale.html', {
            'class_detail': class_detail, 'form': form})

def update_class(request, class_id):
    class_detail = get_object_or_404(Class, pk=class_id)
    if request.method == 'POST':
        form = CreateClass(request.POST, request.FILES, instance=class_detail)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = User.objects.get(username = request.user.get_username())
            post.save()
            return redirect('/createclass/'+str(post.id)+'/addTutor/')
        else:
            return render(request, 'firstApp/update_class.html',{'form': form, 'alert_flag': True})
    else:
        form = CreateClass(instance=class_detail)
        return render(request, 'firstApp/update_class.html', {'class_detail': class_detail, 'form': form})

def community(request):
    if request.user is None:
        redirect('login')
    else:
        b = request.GET.get('b', '')
        c = request.GET.get('c', '')
        k = request.GET.get('k', '')
        cateId = request.GET.get('cateId', '')  # url의 쿼리스트링을 가져온다. 없는 경우 공백을 리턴한다
        cate_list = Category.objects.all()
        bullet_list = Bullet.objects.all()
        best = ''
        if cateId == '':
            post_list = Post.objects.all()
            cateName = '전체 글'
            # 인기글 만드는 함수..
            best = Post.objects.order_by('-views', '-recommendations')

        else:
            post_list = Post.objects.filter(category=cateId)
            cateName = get_object_or_404(Category, pk=cateId).name

        if k:  # k가 있으면
            if c == '1':
                if b:
                    post_list = post_list.filter(bullet=b)
                post_list = post_list.filter(Q(title__icontains=k) | Q(text__icontains=k))  # 작성자에 k가 포함되어 있는 레코드만 필터링
            elif c == '2':
                filtered_author = get_object_or_None(User, username=k)
                if b:
                    post_list = post_list.filter(bullet=b)
                post_list = post_list.filter(author=filtered_author)


        page = request.GET.get('page', 1)
        paginator = Paginator(post_list, 10)
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        return render(request, 'firstApp/community.html', {
            'posts': posts, 'cate_list': cate_list, 'cateName': cateName,
            'cateId': cateId, 'bullets': bullet_list, 'b': b, 'c': c, 'k': k, 'page': page, 'best': best})

def bestPost(request):
    cate_list = Category.objects.all()
    post_list = Post.objects.order_by('-views', '-recommendations')
    page = request.GET.get('page', 1)
    paginator = Paginator(post_list, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'firstApp/community.html', {
       'posts': posts, 'cate_list': cate_list, 'cateName': "인기 글", 'cateId': "0", 'page': page})

def searchResult(request):
    class_list = None
    qq = request.GET.get('qq', '')
    if qq:
        class_list = Class.objects.filter(on_permission=True).filter(Q(title__icontains=qq) | Q(tutor__icontains=qq) |
                                                                 Q(tutor_body__icontains=qq) | Q(body__icontains=qq))

    return render(request, 'firstApp/search.html', {'qq': qq, 'class_list':class_list})

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
       'posts': posts, 'cate_list': cate_list, 'cateName': "내가 쓴 글", 'cateId': "1", 'page': page})

@login_required(login_url='/login/')
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    cateId = request.GET.get('cateId', '')
    page = request.GET.get('page', 1)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = User.objects.get(username=request.user.get_username())
            comment.save()
            return render(request, 'firstApp/post_detail.html', {
                'post': post, 'form': CommentForm(), 'page': page, 'cateId': cateId})
    else:
        form = CommentForm()
        post.views += 1
        post.save()
        return render(request, 'firstApp/post_detail.html', {
            'post': post, 'form': form, 'page': page, 'cateId': cateId})

@login_required(login_url='/login/')
def recommend(request, pk):
    post = get_object_or_404(Post, pk=pk)
    cateId = request.GET.get('cateId', '')
    page = request.GET.get('page', 1)
    if request.user not in post.recommend_user.all():
        post.recommendations += 1
        post.recommend_user.add(request.user)
        post.save()
    return redirect('/community/post/' + str(pk) + '/?cateId=' + str(cateId) + '&page=' + str(page), pk=pk)

@login_required(login_url='/login/')
def no_recommend(request, pk):
    post = get_object_or_404(Post, pk=pk)
    cateId = request.GET.get('cateId', '')
    page = request.GET.get('page', 1)
    if request.user not in post.no_recommend_user.all():
        post.no_recommendations += 1
        post.no_recommend_user.add(request.user)
        post.save()
    return redirect('/community/post/' + str(pk) + '/?cateId=' + str(cateId) + '&page=' + str(page), pk=pk)

@login_required(login_url='/login/')
def createpost(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = User.objects.get(username=request.user.get_username())
            post.save()
        return redirect('community')
    else:
        form = PostForm()
        return render(request, 'firstApp/createpost.html', {'form': form})

def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    cateId = request.GET.get('cateId', '')
    page = request.GET.get('page', 1)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
        return redirect('/community/post/'+str(pk)+'/?cateId='+str(cateId)+'&page='+str(page), pk=pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'firstApp/update_post.html', {'form': form})

def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('community')


def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    cateId = request.GET.get('cateId', '')
    page = request.GET.get('page', 1)
    comment.delete()
    return redirect('/community/post/'+str(comment.post.pk)+'/?cateId='+str(cateId)+'&page='+str(page), pk=comment.post.pk)


def comment_update(request, pk):
    my_comment = get_object_or_404(Comment, pk=pk)
    cateId = request.GET.get('cateId', '')
    page = request.GET.get('page', 1)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=my_comment)
        if form.is_valid():
            form.save()
        return redirect('/community/post/'+str(my_comment.post.pk)+'/?cateId='+str(cateId)+'&page='+str(page), pk=my_comment.post.pk)
    else:
        form = CommentForm(instance=my_comment)
    return render(request, 'firstApp/update_comment.html',
                  {'my_comment': my_comment, 'post': my_comment.post, 'form': form, 'page': page, 'cateId': cateId}
                  )

def create_ccomment(request,pk):
    parent_comment = get_object_or_404(Comment, pk=pk)
    post = get_object_or_404(Post, pk=parent_comment.post.pk)
    cateId = request.GET.get('cateId', '')
    page = request.GET.get('page', 1)
    if request.method == 'POST':
        form = CCommentForm(request.POST)
        if form.is_valid():
            ccomment = form.save(commit=False)
            ccomment.post = post
            ccomment.parent_comment = parent_comment
            ccomment.author = User.objects.get(username=request.user.get_username())
            ccomment.save()
        return redirect('/community/post/'+str(post.pk)+'/?cateId='+str(cateId)+'&page='+str(page), pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'firstApp/create_ccomment.html',
                  {'post': post, 'form': form, 'parent_comment': parent_comment, 'page': page, 'cateId': cateId}
                  )

def remove_ccomment(request, pk):
    ccomment = get_object_or_404(CComment, pk=pk)
    cateId = request.GET.get('cateId', '')
    page = request.GET.get('page', 1)
    ccomment.delete()
    return redirect('/community/post/'+str(ccomment.post.pk)+'/?cateId='+str(cateId)+'&page='+str(page), pk=ccomment.post.pk)

def update_ccomment(request, pk):
    my_ccomment = get_object_or_404(CComment, pk=pk)
    cateId = request.GET.get('cateId', '')
    page = request.GET.get('page', 1)
    if request.method == 'POST':
        form = CCommentForm(request.POST, instance=my_ccomment)
        if form.is_valid():
            form.save()
        return redirect('/community/post/'+str(my_ccomment.post.pk)+'/?cateId='+str(cateId)+'&page='+str(page), pk=my_ccomment.post.pk)
    else:
        form = CCommentForm(instance=my_ccomment)
    return render(request, 'firstApp/update_ccomment.html',
                  {'my_ccomment': my_ccomment, 'post': my_ccomment.post, 'form': form, 'page': page, 'cateId': cateId}
                  )

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/main')
        else:
            return render(request, 'firstApp/login.html', {'loginError': True})
    else:
        return render(request, 'firstApp/login.html')

def signup(request):
    if request.method == "GET":
        return render(request, 'firstApp/signup.html', {'f':SignupForm()} )
    elif request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password']  == form.cleaned_data['password_확인']:
                new_user = User.objects.create_user(form.cleaned_data['username'],form.cleaned_data['email'],form.cleaned_data['password'])
                new_user.name = form.cleaned_data['first_name']
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

@login_required
def delete(request):
    if request.method == 'POST':
        password_form = CheckPasswordForm(request.user, request.POST)
        
        if password_form.is_valid():
            request.user.delete()
            logout(request)
            return redirect('/main')
    else:
        password_form = CheckPasswordForm(request.user)

    return render(request, 'firstApp/delete.html', {'password_form':password_form})

@login_required
def intro_delete(request):
    return render(request, 'firstApp/intro_delete.html')