from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',    include('Index.urls') ),
    path('SMM/',    include('SMM.urls')),
    path('SMQ/',    include('SMQ.urls') ),
    path('Special/',    include('Special.urls') ),
    path('SGQ/',    include('SGQ.urls')),
    path('SGM/',    include('SGM.urls')),
    path('CC/',    include('CC.urls')),
]