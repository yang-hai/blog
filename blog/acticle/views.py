
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse

from acticle.forms import RegisterForm, CgyForm, LoginForm
from acticle.models import Admin, Category, Acticle
from utils.function import is_login


def article(request):
    if request.method == 'GET':
        page = int(request.GET.get('page', 1))
        arts = Acticle.objects.all()
        pg = Paginator(arts, 3)
        arts = pg.page(page)
        cgys = Category.objects.all()
        return render(request, 'article.html', {'arts': arts, 'cgys': cgys})
    if request.method == 'POST':
        return HttpResponseRedirect(reverse('acticle:article'))


def add_acticle(request):
    if request.method == 'GET':
        cgys = Category.objects.all()
        return render(request, 'add-article.html', {'cgys': cgys})
    if request.method == 'POST':
        title = request.POST.get('title')
        contents = request.POST.get('content')
        keywords = request.POST.get('keywords')
        desc = request.POST.get('describe')
        c = request.POST.get('category')
        tags = request.POST.get('tags')
        image = request.FILES.get('titlepic')
        visibility = request.POST.get('visibility')
        Acticle.objects.create(title=title, contents=contents, keyword=keywords,
                               desc=desc, c_id=c, tags=tags, image=image, visibility=visibility)
        if c:
            cgy = Category.objects.filter(pk=c).first()
            cgy.nums += 1
            cgy.save()
        return HttpResponseRedirect(reverse('acticle:add_acticle'))


def update_article(request, id):
    if request.method == 'GET':
        art = Acticle.objects.get(pk=id)
        cgys = Category.objects.all()
        return render(request, 'update-article.html', {'art': art, 'cgys': cgys})
    if request.method == 'POST':
        title = request.POST.get('title')
        contents = request.POST.get('content')
        keywords = request.POST.get('keywords')
        desc = request.POST.get('describe')
        c = request.POST.get('category')
        tags = request.POST.get('tags')
        image = request.FILES.get('titlepic')
        visibility = request.POST.get('visibility')
        art = Acticle.objects.filter(pk=id).first()
        art.title = title
        art.contents = contents
        art.keyword = keywords
        art.desc = desc
        if c:
            if art.c_id != c:
                c_id = art.c_id
                cgy = Category.objects.filter(pk=c_id).first()
                cgy.nums -= 1
                cgy.save()
                art.c_id = c
                cgy = Category.objects.filter(pk=c).first()
                cgy.nums += 1
                cgy.save()
        art.tags = tags
        art.image = image
        art.visibility = visibility
        art.save()
        return HttpResponseRedirect(reverse('acticle:article'))


def del_article(request, id):
    if request.method == 'GET':
        art = Acticle.objects.filter(pk=id)
        c_id = art.c_id
        cgy = Category.objects.filter(pk=c_id).first()
        cgy.nums -= 1
        cgy.save()
        art.delete()
        return HttpResponseRedirect(reverse('acticle:article'))


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            Admin.objects.create(username=username, password=password)
            return HttpResponseRedirect(reverse('acticle:login'))
        else:
            errors = form.errors
            return render(request, 'register.html', {'errors': errors})


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            admin = Admin.objects.filter(username=username).first()
            request.session['admin_id'] = admin.id
            return HttpResponseRedirect(reverse('acticle:article'))
        else:
            errors = form.errors
            return render(request, 'login.html', {'errors': errors})


def logout(request):
    if request.method == 'GET':
        # 1.删除cookie中的sessionid值
        # 2.删除django_session表中的数据
        # 3.删除django_session中session_data中的user_id
        request.session.flush()  # 清除当前会话数据
        # del request.session['admin_id']  # 删除单个key
        # request.session.clear()  # 清除所有会话,但不会删除数据
        return HttpResponseRedirect(reverse('acticle:login'))


def add_category(request):
    if request.method == 'GET':
        cgys = Category.objects.all()
        if cgys:
            for cgy in cgys:
                if cgy.f_id:
                    total = Acticle.objects.filter(c=cgy.id).count()
                    cgy.nums = total
                    cgy.save()
        return render(request, 'category.html', {'cgys': cgys})
    if request.method == 'POST':
        form = CgyForm(request.POST)
        if form.is_valid():
            c_name = form.cleaned_data['cname']
            f = request.POST.get('fid')
            alias = form.cleaned_data['alias']
            keywords = form.cleaned_data['keywords']
            desc = form.cleaned_data['describe']
            Category.objects.create(c_name=c_name, f_id=f, alias=alias, keywords=keywords, desc=desc)
            return HttpResponseRedirect(reverse('acticle:add_category'))
        else:
            errors = form.errors
            return render(request, 'category.html', {'errors': errors})


def del_category(request, id):
    if request.method == 'GET':
        cgy = Category.objects.filter(pk=id)
        arts = Acticle.objects.all()
        cgys = Category.objects.all()
        for art in arts:
            if art.c_id == id:
                art.delete()
        for cgy in cgys:
            if cgy.f_id == id:
                cgy.delete()
        cgy.delete()
        return HttpResponseRedirect(reverse('acticle:add_category'))


def update_category(request, id):
    if request.method == 'GET':
        currentcgy = Category.objects.get(pk=id)
        fcgy = Category.objects.filter(pk=currentcgy.f_id).first()
        f_c_name = '无'
        if fcgy:
            f_c_name = fcgy.c_name
        cgys = Category.objects.all()
        return render(request, 'update-category.html',
                      {'currentcgy': currentcgy, 'f_c_name': f_c_name, 'cgys': cgys})
    if request.method == 'POST':
        search = request.POST.get('search')
        if not search:
            c_name = request.POST.get('name')
            alias = request.POST.get('alias')
            f = request.POST.get('fid')
            keywords = request.POST.get('keywords')
            desc = request.POST.get('describe')
            Category.objects.filter(pk=id).update(c_name=c_name, f_id=f, alias=alias, keywords=keywords, desc=desc)
        return HttpResponseRedirect(reverse('acticle:add_category'))

