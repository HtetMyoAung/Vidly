from django.db import models
from django.utils import timezone


class Genre(models.Model):
    name = models.CharField(max_length=255)  # ဇာတ်အမျိုးအစားနာမည် (စာသား)

    def __str__(self):
        return self.name  # Genre object ကို string အဖြစ်ပြသတဲ့အခါ name ကိုပြသပါမယ်


class Movie(models.Model):  # models.Model ကို Inherit (အမွေယူ) လုပ်ရပါတယ်
    title = models.CharField(max_length=255)      # ရုပ်ရှင်နာမည် (စာသား)
    release_year = models.IntegerField()          # ထွက်ရှိတဲ့နှစ် (ကိန်းပြည့်)
    number_in_stock = models.IntegerField()       # ဆိုင်မှာရှိတဲ့ အရေအတွက်
    daily_rate = models.FloatField()              # တစ်ရက်ငှားရမ်းခ (ဒသမကိန်း)
    # ဇာတ်အမျိုးအစား (အမှတ်)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    date_created = models.DateTimeField(
        default=timezone.now)  # ဖန်တီးသည့်ရက်စွဲ (အချိန်)

    def __str__(self):
        return self.title  # Movie object ကို string အဖြစ်ပြသတဲ့အခါ title ကိုပြသပါမယ်
