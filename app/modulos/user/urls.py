from django.urls import path

from .views import *

app_name = 'user'
urlpatterns = [
    path('cadastrar_user/', user_cadastro, name='cadastrar_user'),
]