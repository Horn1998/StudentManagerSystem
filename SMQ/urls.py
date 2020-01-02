from django.urls import path, re_path
from . import views
urlpatterns = [
    path('',views.SMQView, name = 'SMQ'),
    path('find_message',views.find_message),

]