from django.shortcuts import render,HttpResponse,redirect
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.generics import *
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


class GoodsTypeList(APIView):
    def get(self,request):
        goodstype_list = GoodsType.objects.all()
        serializer_data = GoodsTypeSerializer(goodstype_list,many=True)
        return Response(serializer_data.data)

    def post(self,request):
        data = request.data

        # name = request.POST.get('goodstype_name')
        # img = request.FILES.get('goodstype_img')
        # goodstype_obj = GoodsType(name=name,logo=img)
        # goodstype_obj.save()
        ser_data = GoodsTypeSerializer(data=data)
        print(ser_data)
        if ser_data.is_valid():
            print('符合要求')
            ser_data.save()
            return redirect('/seller/goodstype')
        else:
            return Response({"status":'error'})


def vue(request):
    return render(request,'seller/vuetest.html')