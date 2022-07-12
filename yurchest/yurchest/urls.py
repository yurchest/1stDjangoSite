from django.contrib import admin
from django.urls import path
from django.urls import include

from main.views import pageNotFound


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

handler404 = pageNotFound
