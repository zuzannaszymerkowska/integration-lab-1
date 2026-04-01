from django.contrib import admin
from django.urls import path, include
from external_data.views import weather_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('weather/', weather_view, name='weather'),
]