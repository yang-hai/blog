# 装饰器，闭包
# 1.外层函数内嵌内层函数
# 2.外层函数返回的是内层函数
# 3.内层函数调用外层函数的参数
from django.http import HttpResponseRedirect
from django.urls import reverse


def is_login(func):
    def check_status(request):
        if request.session.get('user_id'):
            return func(request)
        else:
            return HttpResponseRedirect(reverse('acticle:login'))
    return check_status
