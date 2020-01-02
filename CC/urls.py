from django.urls import path, re_path
from . import views
urlpatterns = [
    path('',views.CCView, name = 'CC'),
    path('courses',views.get_Courses),
    path('choiceclass', views.CCS),

]