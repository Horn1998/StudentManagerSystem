from django.urls import path, re_path
from . import views
urlpatterns = [
    path('',views.SpecialView, name = 'Special'),
    path('special', views.special_process)
]