from django.contrib import admin
from django.urls import path
from .views import home, count, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name='home' ),
    path('count/',count, name='count'),
    path('about/',about,name='about'),
]
