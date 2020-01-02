from django.urls import path, re_path
from . import views
urlpatterns = [
    path('',views.SGQView, name = 'SGQ'),
    path('get_Class', views.get_class),
    path('find_message', views.find_message),
    path('find_class', views.find_class),
    path('export', views.export)
]