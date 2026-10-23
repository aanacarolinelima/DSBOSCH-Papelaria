from django.urls import path
from .views import listar_categorias, listar_produtos

urlpatterns =[ 
     path ('categorias', listar_categorias)
]

urlpatterns =[ 
     path ('produtos', listar_produtos )
]