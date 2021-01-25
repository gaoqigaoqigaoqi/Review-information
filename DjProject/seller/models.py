from django.db import models

"""
verbose_name 别名，在后台可以使用
unique 不可以重复
blank 可以为空 常用于字符串
null 可以为null 常用于数字和时间
auto_now 默认当前时间
django orm 默认自带id、默认字段不为空
"""
# Create your models here.
class Seller(models.Model):
    username = models.CharField(max_length=32,default='zs')
    password = models.CharField(max_length=64,default='222')
    phone = models.CharField(max_length=32,default='110')
    address = models.CharField(max_length=128,default='北京市')
    gender = models.BooleanField(default=True) # 默认为True是男
    # upload 上传用户图片到哪个目录
    headimg = models.ImageField(upload_to='seller/headimg',default='1.jpg')


class Store(models.Model):
    name = models.CharField(max_length=32,default='我的小店')
    address = models.CharField(max_length=128, default='广州')
    desc = models.CharField(max_length=128, default='不咋地')
    logo = models.ImageField(upload_to='seller/storeimg', default='1.jpg')
    # 设置卖家和店铺一对一
    seller = models.OneToOneField(to=Seller,on_delete=models.CASCADE)


class GoodsType(models.Model):
    name = models.CharField(max_length=64)
    logo = models.ImageField(upload_to='seller/goodstypeimg',default='1.jpg')


class Goods(models.Model):
    name = models.CharField(max_length=32,default='苹果')
    price = models.DecimalField(max_digits=5,decimal_places=2) # 价格 总共5位小数2位
    bzq = models.IntegerField(default=30) # 保质期
    scrq = models.DateField(null=True,blank=True) # 生产日期
    desc = models.CharField(max_length=128,default='商品描述....')
    content = models.TextField(default='商品详情...')
    # ImageField要和pillow同步使用不然同步数据库会报错
    image = models.ImageField(upload_to='seller/goodsimg',default='1.jpg')
    # 商品类型和商品是一对多关系
    goodstype = models.ForeignKey(to=GoodsType,on_delete=models.CASCADE)
    # 店铺和商品是一对多关系
    store = models.ForeignKey(to=Store,on_delete=models.CASCADE,null=True,blank=True)

