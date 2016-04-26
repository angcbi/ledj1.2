# -*- coding:utf-8 -*-

from django import forms


class UserForm(forms.Form):
    username = forms.CharField('姓名')
    headimg = forms.FileField('选择文件')


class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)

