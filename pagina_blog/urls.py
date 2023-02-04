from django.urls import path, include
from pagina_blog.views import (
  inicio,listar_noticias,NoticiaCreateView, 
  buscar_noticias,ver_noticia, NoticiaEditView , NoticiaDeleteView,mi_info
)

urlpatterns = [
  path('Noticias/', listar_noticias, name='listar_noticias'),
  path('Publicar/', NoticiaCreateView.as_view(), name= 'publicar_noticias'),
  path('Buscar/', buscar_noticias, name= 'buscar_noticias'),
  path('Ver/<int:id>', ver_noticia, name= 'ver_noticia'),
  path('Editar-Noticia/<int:pk>', NoticiaEditView.as_view(), name= 'editar_noticia'),
  path('Eliminar-Noticia/<int:pk>', NoticiaDeleteView.as_view(), name='eliminar_noticia'),

  path('Acerca-de-mi/', mi_info, name='about')
]

