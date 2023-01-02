from django.urls import path
from .views import (
    pessoal,
    departamentos,
    crt_dep,
    departamento,
    delete_dpto,
    colaboradores_,
    crtcolab,
    atzcolab,
    delcolab,
    relcols,
    crtrelcols,
    lstrelcols,
    delrelcols,
    )

urlpatterns = [
    path('', pessoal),
    path('departamentos/', departamentos),
    path('departamentos/criacao/', crt_dep),
    path('departamento/<str:id>/', departamento),
    path('departamento/delete/<str:id>/', delete_dpto),
    path('colaboradores/', colaboradores_),
    path('colaborador/criacao/', crtcolab),
    path('colaborador/atualizacao/<str:id>/', atzcolab),
    path('colaborador/delete/<str:id>/', delcolab),
    path('relacionamentos/', relcols),
    path('relacionamentos/criacao/', crtrelcols),
    path('relacionamentos/listagem/', lstrelcols),
    path('relacionamentos/delecao/<str:id>/', delrelcols),
]