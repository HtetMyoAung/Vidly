from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Movie, Genre


# say_hello ဆိုတဲ့ function တစ်ခု ဆောက်လိုက်တာပါ (နာမည်ကြိုက်တာပေးလို့ရတယ်)
def say_hello(request):
    movies = Movie.objects.all()  # Movie model ထဲက အားလုံးကို ရယူပါ
    genres = Genre.objects.all()  # Genre model ထဲက အားလုံးကို ရယူပါ
    # movies/index.html ကို render လုပ်ပြီး movies နဲ့ genres ကို context အဖြစ်ပေးပါ
    return render(request, 'movies/index.html', {'movies': movies, 'genres': genres})


def movie_detail(request, movie_id):
   # movie_id နဲ့ ကိုက်ညီတဲ့ Movie object ကို ရယူပါ။ မတွေ့ရင် 404 error ပြပါ
    movie = get_object_or_404(Movie, id=movie_id)
    # movies/detail.html ကို render လုပ်ပြီး movie ကို context အဖြစ်ပေးပါ
    return render(request, 'movies/detail.html', {'movie': movie})
