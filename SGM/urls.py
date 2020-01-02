from django.urls import path, re_path
from . import views
urlpatterns = [
    path('',views.SGMView),
    path('insert_grade', views.insert_message),
    path('get_Class', views.get_class),
    path('get_Grade', views.get_grade),
    path('get_Delete_Class', views.get_delete),
    path('delete_grade', views.delete_message),
]