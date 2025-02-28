from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('datetime/', views.curr_datetime, name='datetime'),
    path('', views.index, name='index')
]
