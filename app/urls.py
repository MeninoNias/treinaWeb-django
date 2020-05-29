from django.urls import path, include

from . import views

app_name = 'app'
urlpatterns = [
    path('', views.index),
    path('index/', include('app.modulos.urls', namespace='gerenciador')),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]