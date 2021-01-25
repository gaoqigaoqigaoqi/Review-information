from django import forms
from django.core.exceptions import ValidationError
class SellerForm(forms.Form):
    username = forms.CharField(
        required=True, # 必填
        error_messages={"required":"不能为空"},

    )
    password = forms.CharField(
        required=True,
        min_length=6,# 最少6位
        error_messages={"required":"不能为空","min_length":"密码至少6位"}
    )
    email = forms.CharField(
        required=True,
        error_messages={"required": "不能为空"}
    )
    phone = forms.CharField(
        required=True,
        error_messages={"required":"不能为空"}
    )
    address = forms.CharField(
        required=True,
        error_messages={"required": "不能为空"}
    )
    gender = forms.CharField(
        required=True,
        error_messages={'required': '不能为空'},
    )
    headimg=forms.ImageField(
        required=True,
        error_messages={'required': '未上传头像'},
    )

    # 自定义校验方法
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if 'zz' in username:
            raise ValidationError('昵称违规')
