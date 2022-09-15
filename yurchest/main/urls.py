from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.decorators import login_required
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register(r'news-api', NewsAPIViewSet)


urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('messages/', Messages.as_view(), name='messages'),
    path('news', News_view.as_view(), name='news'),
    path('str3', Str3.as_view(), name='str3'),
    path('about/', about, name='about'),
    path('curriculum', Curriculum.as_view(), name='cv'),
    path('register/', register, name='register'),
    path('api/', include(router.urls)),
]

urlpatterns += staticfiles_urlpatterns()
