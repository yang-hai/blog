from django.core import serializers
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse

from acticle.models import Category, Acticle
from user.forms import RegisterForm, LoginForm
from user.models import User


def register(request):
    if request.method == 'GET':
        return render(request, 'user-register.html')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            User.objects.create(username=username, password=password)
            return HttpResponseRedirect(reverse('user:login'))
        else:
            errors = form.errors
            return render(request, 'user-register.html', {'errors': errors})


def login(request):
    if request.method == 'GET':
        return render(request, 'user-login.html')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            user = User.objects.filter(username=username).first()
            request.session['user_id'] = user.id
            return HttpResponseRedirect(reverse('user:index'))
        else:
            errors = form.errors
            return render(request, 'user-login.html', {'errors': errors})


def logout(request):
    if request.method == 'GET':
        del request.session['user_id']
        return HttpResponseRedirect(reverse('user:login'))


def index(request):
    if request.method == 'GET':
        cgys = Category.objects.all()
        arts = Acticle.objects.all()
        return render(request, 'user-index.html', {'cgys': cgys, 'arts': arts})
    if request.method == 'POST':
        pass


def article_list(request):
    if request.method == 'GET':
        cgys = Category.objects.all()
        arts = Acticle.objects.all()
        cid = request.GET.get('cid', 0)
        if cid != 0:
            cgy = Category.objects.get(pk=cid)
            arts = cgy.acticle_set.all()
            page = request.GET.get('page', 1)
            pg = Paginator(arts, 1)
            arts = pg.page(page)
            return render(request, 'list.html', {'cgys': cgys, 'arts': arts, 'cgy': cgy})
        page = request.GET.get('page', 1)
        pg = Paginator(arts, 1)
        arts = pg.page(page)
        return render(request, 'list.html', {'cgys': cgys, 'arts': arts})
    if request.method == 'POST':
        pass


def info(request, id):
    if request.method == 'GET':
        index_num = request.GET.get('num')
        page = request.GET.get('page')
        if index_num:
            index_num = int(index_num)
        arts = Acticle.objects.all().order_by('create_time')
        arts_list = list(arts)
        art_pre = 0
        art_next = 0
        if id:
            page = int(page)
            art = Acticle.objects.get(pk=id)
            index_num = arts_list.index(art)
            if page == -1:
                index_num -= 1
                art = arts_list[index_num]
                if index_num > 1:
                    art_pre = arts_list[index_num-1]
                art_next = arts_list[index_num + 1]
            if page == 1:
                index_num += 1
                art = arts_list[index_num]
                if art != arts_list[-1]:
                    art_next = arts_list[index_num + 1]
                art_pre = arts_list[index_num - 1]
        else:
            if not index_num:
                art = arts_list[0]
                index_num = 0
                art_next = arts_list[index_num + 1]
        f_c_name = Category.objects.filter(pk=art.c_id).first().c_name
        return render(request, 'info.html', {'art': art, 'f_c_name': f_c_name,
                                             'index_num': index_num, 'art_pre': art_pre,
                                             'art_next': art_next})


def category(request):
    if request.method == 'GET':
        cgys = Category.objects.all()
        cgys = serializers.serialize("json", cgys)
        return JsonResponse({'code': 200, 'msg': '请求成功', 'cgys': cgys})
