from django.contrib import admin
from .models import Movie, Genre  # Movie နှင့် Genre models ကို import လုပ်တာပါ


class MovieAdmin(admin.ModelAdmin):
 # admin panel မှာ Movie objects တွေကို ဘယ် field တွေပြသမလဲ ဆိုတာကို သတ်မှတ်တာပါ
    list_display = ('title', 'release_year',
                    'number_in_stock', 'daily_rate', 'genre')


class GenreAdmin(admin.ModelAdmin):
    # Genre objects တွေကို name field နဲ့ပြသဖို့သတ်မှတ်တာပါ
    list_display = ('id', 'name')


# Movie model ကို admin panel မှာ ပြသဖို့ register လုပ်တာပါ
admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre, GenreAdmin)  # Genre model ကိုလည်း register လုပ်တာပါ
