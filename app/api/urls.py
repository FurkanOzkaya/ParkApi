
from django.contrib import admin
from django.urls import include, path
from app.api.views import ParkApi
from app.api.views import ParkApiList

urlpatterns = [
    path('get_spesific_park_area/<pk>', ParkApi.as_view()),
    path('add_park_area', ParkApi.as_view()),
    path('display_close_areas', ParkApiList.as_view()),
    path('delete_areas/<pk>', ParkApi.as_view()),
]
