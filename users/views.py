from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.
class reqsers(View):

    def get(self,request):
        username = request.GET.get('username')
        password = request.GET.get('password')
        print(username,password)
        return HttpResponse('测试接收查询字符串数据')
    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        return HttpResponse('测试接收表单数据')