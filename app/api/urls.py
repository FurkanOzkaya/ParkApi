
from django.contrib import admin
from django.urls import include, path
from app.api.views import ParkApi

urlpatterns = [
    path('display_all', ParkApi.as_view()),
    path('add_park_area', ParkApi.as_view()),
    path('display_close_areas', ParkApi.as_view()),
    path('delete_areas', ParkApi.as_view()),
]
