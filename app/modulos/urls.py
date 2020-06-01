from django.urls import path, include

app_name = 'gerenciador'
urlpatterns = [
    path('', include('app.modulos.tarefa.urls', namespace='tarefa')),
    path('user/', include('app.modulos.user.urls', namespace='user')),
]