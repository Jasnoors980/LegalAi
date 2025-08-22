from django.urls import path
from .views import index

urlpatterns = [
    path('sum/', index, name='index'),
]
