"""
URL configuration for vidly project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include  # include ကို import လုပ်တာပါ
from api.models import MovieResource  # MovieResource ကို import လုပ်တာပါ

movie_resource = MovieResource()  # MovieResource ကို instance တစ်ခု ဖန်တီးတာပါ
urlpatterns = [
    path('admin/', admin.site.urls),
    # 'movies/' လို့ လှမ်းခေါ်ရင် movies app ရဲ့ urls.py ကို include လုပ်တာပါ
    path('movies/', include('movies.urls')),
    # ဒီလမ်းကြောင်းက Tastypie ရဲ့ API အတွက် ဖြစ်ပါတယ်
    # movie_resource.urls ထဲမှာ GET, POST, PUT, DELETE လမ်းကြောင်းတွေ အကုန်အသင့် ပါပြီးသားပါ
    path('api/', include(movie_resource.urls)),
]
