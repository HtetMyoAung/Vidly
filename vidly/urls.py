from django.contrib import admin
from django.urls import path, include  # include ကို import လုပ်တာပါ
from api.models import MovieResource  # MovieResource ကို import လုပ်တာပါ
from . import views

movie_resource = MovieResource()  # MovieResource ကို instance တစ်ခု ဖန်တီးတာပါ
urlpatterns = [
    # homepage
    path('', views.home),
    path('admin/', admin.site.urls),
    # 'movies/' လို့ လှမ်းခေါ်ရင် movies app ရဲ့ urls.py ကို include လုပ်တာပါ
    path('movies/', include('movies.urls')),
    # ဒီလမ်းကြောင်းက Tastypie ရဲ့ API အတွက် ဖြစ်ပါတယ်
    # movie_resource.urls ထဲမှာ GET, POST, PUT, DELETE လမ်းကြောင်းတွေ အကုန်အသင့် ပါပြီးသားပါ
    path('api/', include(movie_resource.urls)),

]
