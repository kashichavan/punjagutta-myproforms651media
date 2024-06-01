from django.urls import path
from .views import empreg
app_name='app1'

urlpatterns = [
    path('reg/',empreg),
]
