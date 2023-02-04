from django.urls import path, include
from usuarios.views import registro, login_view, CustomLogoutView, ProfileUpdateView, agregar_avatar


urlpatterns = [
    path('registro/', registro, name="registro"),
    path('login/', login_view, name="login"),
    path('logout/', CustomLogoutView.as_view(), name="logout"),
    path('Editar-Perfil/', ProfileUpdateView.as_view(), name="editar_perfil"),
    path('Agregar-Perfil/', agregar_avatar, name="agregar_avatar")
]