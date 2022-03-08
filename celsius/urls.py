from django.urls import path
from .views import *


urlpatterns = [
    path('', main, name='main'),
    path('celsius/', celsius, name='celsius'), # 127.0.0.2:8000/celsius/
]
