from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie, Genre


# say_hello ဆိုတဲ့ function တစ်ခု ဆောက်လိုက်တာပါ (နာမည်ကြိုက်တာပေးလို့ရတယ်)
def say_hello(request):
    movies = Movie.objects.all()  # Movie model ထဲက အားလုံးကို ရယူပါ
    # ရုပ်ရှင်နာမည်တွေကို comma နဲ့ ခွဲပြီး string ပြောင်းပါ
    output = ', '.join([movie.title for movie in movies])
    return HttpResponse(output)  # HTTP response အဖြစ် ရုပ်ရှင်
