from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# say_hello ဆိုတဲ့ function တစ်ခု ဆောက်လိုက်တာပါ (နာမည်ကြိုက်တာပေးလို့ရတယ်)
def say_hello(request):
    return HttpResponse("Hello World")
