from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
# Create your views here.
class asdfgs(View):
    def get(self,request):
        username = request.GET.get('username')
        password = request.GET.get('password')
        print(username,password)
        return HttpResponse('测试接收查询字符串数据')

    def post(self,request):
        username = request.GET.get('username')
        password = request.GET.get('password')
        print(username, password)

        return HttpResponse('测试接收表单数据')