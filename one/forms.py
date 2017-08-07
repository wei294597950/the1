#coding:utf-8
from django import forms

clusters = (
  ('es_offline', 'es_offline'),
  ('es_online', 'es_online'),
)
indexs=(
        ("chat_test","chat_test"),
        ("chat_test2","chat_test2"),
)
class addform(forms.Form):
        name = forms.ChoiceField(choices=clusters,label="集群", error_messages={"required": "这个项必须填写"})
        address = forms.ChoiceField(choices=indexs,label="地址", error_messages={"required": "这个项必须填写"})
        city = forms.CharField(label="城市", error_messages={"required": "这个项必须填写"})
        state_province = forms.CharField(label="省份", error_messages={"required": "这个项必须填写"})
        country = forms.CharField(label="国家", error_messages={"required": "这个项必须填写"})
        website = forms.URLField(label="网址", error_messages={"required": "这个项必须填写"})




class editform(forms.Form):
    cluster = forms.DateTimeField()
    index=forms.CharField(label="index")
    types=forms.CharField(label="types")
    qaid=forms.CharField(label="id")
    newanswer=forms.CharField(label="new answer")

from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        label="用户名",
        error_messages={'required': '请输入用户名'},
        widget=forms.TextInput(
            attrs={
                'placeholder':"用户名",
            }
        ),
    )
    password = forms.CharField(
        required=True,
        label="密码",
        error_messages={'required': '请输入密码'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder': "密码",
            }
        ),
    )
    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError("用户名和密码为必填项")
        else:
            cleaned_data = super(LoginForm, self).clean()