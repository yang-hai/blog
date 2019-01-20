from django import forms
from django.contrib.auth.hashers import make_password, check_password

from acticle.models import Admin, Category


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=10,
                               min_length=2,
                               required=True,
                               error_messages={
                                   'required': '用户名必填',
                                   'max_length': '最大长度10字符',
                                   'min_length': '最小长度2字符'
                               })
    password = forms.CharField(max_length=150,
                               min_length=6,
                               required=True,
                               error_messages={
                                   'required': '密码必填',
                                   'max_length': '最大长度150字符',
                                   'min_length': '最小长度6字符'
                               })
    password2 = forms.CharField(max_length=150,
                                min_length=6,
                                required=True,
                                error_messages={
                                    'required': '确认密码必填',
                                    'max_length': '最大长度150字符',
                                    'min_length': '最小长度6字符'
                                })

    def clean(self):
        username = self.cleaned_data.get('username')
        adm = Admin.objects.filter(username=username).first()
        if adm:
            raise forms.ValidationError({'username': '用户名已存在'})
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError({'password2': '密码不一致'})
        self.cleaned_data['password'] = make_password(password)
        return self.cleaned_data


class CgyForm(forms.Form):
    cname = forms.CharField(max_length=10,
                            min_length=2,
                            required=True,
                            error_messages={
                                'required': '栏目名称必填',
                                'max_length': '最大长度50字符',
                                'min_length': '最小长度2字符'
                            })
    alias = forms.CharField(max_length=10,
                            required=False,
                            error_messages={
                                'max_length': '最大长度10字符'
                            })
    keywords = forms.CharField(max_length=20,
                               required=False,
                               error_messages={
                                   'max_length': '最大长度20字符'
                               })
    describe = forms.CharField(max_length=200,
                               required=False,
                               error_messages={
                                   'max_length': '最大长度200字符'
                               })

    def clean_name(self):
        c_name = self.cleaned_data['cname']
        cgy = Category.objects.filter(c_name=c_name).first()
        if cgy:
            raise forms.ValidationError('栏目名已存在')
        return self.cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(max_length=10,
                               min_length=2,
                               required=True,
                               error_messages={
                                   'required': '用户名必填',
                                   'max_length': '最大长度10字符',
                                   'min_length': '最小长度2字符'
                               })
    userpwd = forms.CharField(max_length=150,
                              min_length=6,
                              required=True,
                              error_messages={
                                  'required': '密码必填',
                                  'max_length': '最大长度150字符',
                                  'min_length': '最小长度6字符'
                              })

    def clean(self):
        username = self.cleaned_data['username']
        adm = Admin.objects.filter(username=username).first()
        if not adm:
            raise forms.ValidationError({'username': '用户名不存在'})
        userpwd = self.cleaned_data.get('userpwd')
        admin = Admin.objects.filter(username=username).first()
        if not check_password(userpwd, admin.password):
            raise forms.ValidationError({'userpwd': '密码不正确'})
        return self.cleaned_data
