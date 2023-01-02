from django.urls import path, include
from .views import lgn, lgt

urlpatterns = [
    path('login/', lgn),
    path('logout/', lgt),
]
