import re
import time
import logging

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

from acticle.models import Admin


# 获取处理日志的logger
from user.models import User

logger = logging.getLogger(__name__)


class TestMiddleware1(MiddlewareMixin):

    def process_request(self, request):
        # 对所有的请求都进行登录状态校验
        path = request.path
        if path == '/':
            return None
        not_need_check = ['/static/.*', '/media/.*']
        for check_path in not_need_check:
            if re.match(check_path, path):
                return None
        if re.match('/acticle/.*', path):
            if path in ['/acticle/register/', '/acticle/login/']:
                return None
            try:
                admin_id = request.session['admin_id']
                admin = Admin.objects.get(pk=admin_id)
                request.user = admin
            except:
                return HttpResponseRedirect(reverse('acticle:login'))
        if path in ['/user/register/', '/user/login/', '/user/category/']:
            return None
        try:
            user_id = request.session['user_id']
            user = User.objects.get(pk=user_id)
            request.user = user
        except:
            return HttpResponseRedirect(reverse('user:login'))


class LoggingMiddleware(MiddlewareMixin):

    def process_request(self, request):
        request.init_time = time.time()

    def process_response(self, request, response):
        try:
            # 请求到响应之间消耗时长
            count_times = time.time() - request.init_time
            # 请求地址和请求方式
            path = request.path
            method = request.method
            # 响应的状态码和内容
            status = response.status_code
            content = response.content
            # 日志记录的信息
            message = '%s %s %s %s %s' % (path, method, status, content, count_times)
            logger.info(message)
        except Exception as e:
            logger.critical('log error: %s' % e)
        return response
