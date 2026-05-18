from django.urls import path
from . import views  # လက်ရှိ folder ထဲက views.py ကို ယူသုံးတာပါ

urlpatterns = [
    # path က အလွတ်ထားရပါမယ်။ ဘာလို့လဲဆိုတော့ Project ရဲ့ urls.py ကနေ 'movies/' လို့ လှမ်းခေါ်မှာမို့လို့ပါ
    path('', views.say_hello, name='index'),
]
