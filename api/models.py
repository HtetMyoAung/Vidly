from django.db import models
from tastypie.resources import ModelResource
from movies.models import Movie


class MovieResource(ModelResource):
    class Meta:
        queryset = Movie.objects.all()  # ဒီမှာတင် ဒေတာအားလုံးကို ဆွဲထုတ်ခိုင်းလိုက်တယ်
        resource_name = 'movies'
        # date_created ကို API မှာ မပါဝင်အောင် ထည့်လိုက်တယ်
        excludes = ['date_created']
