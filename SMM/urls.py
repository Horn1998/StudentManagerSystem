from django.urls import path, re_path
from . import views
urlpatterns = [
    path('',views.SMMView, name = 'SMM'),
    path('insert_message', views.insert_message),
    path('delete_message', views.delete_message),
    path('change_message', views.change_message),
    path('find_message', views.find_message),

]