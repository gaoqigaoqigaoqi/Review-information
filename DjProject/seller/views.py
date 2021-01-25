from django.shortcuts import render,HttpResponse,redirect
from rest_framework.response import Response
from rest_framework import generics
from .models import *
from rest_framework.views import APIView
from .serializers import SellerSerializer
# Create your views here.
from .form import SellerForm

class Register(APIView):
    def get(self,request,*args,**kwargs):
        return render(request,'seller/register.html')

    def post(self,request):
        data = request.data
        sellerform = SellerForm(request.POST,request.FILES)
        if sellerform.is_valid():
            user = SellerSerializer(data=data)
            if user.is_valid():
                # user.save()
                print('注册成功')
                return redirect('/seller/login/')
            else:
                return redirect('/seller/register/')
        print('出现异常')
        return render(request,'seller/register.html/',{"sellerform":sellerform})


class Login(APIView):
    def get(self,request):
        print('我是login get')
        return render(request,'seller/login.html')
    def post(self,request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        print('我是login post')
        print(username,password)
        seller_obj = Seller.objects.get(username=username,password=password)
        if seller_obj:
            response = redirect('/seller/index/')
            response.set_cookie("username", username)
            response.set_cookie("id", seller_obj.id)
            response.set_cookie("img",seller_obj.headimg.name)
            return response
        else:
            return Response({"status":"error"})

class Index(APIView):
    def get(self,request):
        return render(request,'seller/index.html')