from django.contrib.auth import get_user_model
# AUTH_USERMODELを設定した際にのみ使える関数
from django.contrib.auth.forms import UserCreationForm
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
       model = get_user_model()
       fields = ('email',)

class AddToCartForm(forms.Form):
    num = forms.IntegerField( 
        label='数量',
        min_value=1,
        required=True)
        # 必須項目

# 追加
class PurchaseForm(forms.Form):
    zip_code = forms.CharField(
        label='郵便番号',
        max_length=7,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': '数字 7 桁(ハイフンなし)'}))
    
    address = forms.CharField(
        label='住所', 
        max_length=100,
        required=False)