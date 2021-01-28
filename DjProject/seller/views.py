from django.shortcuts import render,HttpResponse,redirect
from rest_framework.response import Response
from rest_framework import generics
from .models import *
from rest_framework.views import APIView
from .serializers import *
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
                user.save()
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
        print('我是login post')
        username = request.POST.get("username")
        password = request.POST.get("password")
        seller_obj = Seller.objects.get(username=username,password=password)
        if seller_obj:
            seller_data = SellerSerializer(seller_obj)
            response = redirect('/seller/index/')
            response.set_cookie("username", username)
            response.set_cookie("id", seller_obj.id)
            response.set_cookie("img",seller_obj.headimg.name)
            return response


class Index(APIView):
    def get(self,request):
        return render(request,'seller/index.html')


def goodstype(request):

    return render(request,'seller/goods_type_list.html')

class GoodsTypeList(generics.ListAPIView):
    serializer_class = GoodsTypeSerializer
    def get_queryset(self):
        goodstypes = GoodsType.objects.all()
        return goodstypes


    def get_serializer_context(self):
        return {
            'view':self
        }

class AddGoods(generics.CreateAPIView):
    pass



def vue(request):
    return render(request,'seller/vuetest.html')