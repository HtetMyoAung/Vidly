from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie, Genre


# say_hello ဆိုတဲ့ function တစ်ခု ဆောက်လိုက်တာပါ (နာမည်ကြိုက်တာပေးလို့ရတယ်)
def say_hello(request):
    movies = Movie.objects.all()  # Movie model ထဲက အားလုံးကို ရယူပါ
    genres = Genre.objects.all()  # Genre model ထဲက အားလုံးကို ရယူပါ
    # movies/index.html ကို render လုပ်ပြီး movies နဲ့ genres ကို context အဖြစ်ပေးပါ
    return render(request, 'movies/index.html', {'movies': movies, 'genres': genres})


def movie_detail(request, movie_id):
    # movie_id နဲ့ ကိုက်တဲ့ Movie ကို ရယူပါ
    movie = Movie.objects.get(id=movie_id)
    # movies/detail.html ကို render လုပ်ပြီး movie ကို context အဖြစ်ပေးပါ
    return render(request, 'movies/detail.html', {'movie': movie})
