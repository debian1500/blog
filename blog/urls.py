from django.contrib import admin
from django.urls import path
from main import views
from django.conf import settings
from django.conf.urls.static import static
   
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_URL)
