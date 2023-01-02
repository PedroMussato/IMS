from django.urls import path
from .views import (
    ativos,
    classes, crtcls, lstcls, atzcls, delcls,
    brds, crtbrd, lstbrd, atzbrd, delbrd,
    gestao, crtatv, lstatv, atzatv, delatv,
    pacotes, crtpkg, lstpkg, atzpkg, mngpkg, clspkg, delpkg,
)


urlpatterns = [
    path('', ativos),
    path('classes/', classes),
    path('classes/criacao/', crtcls),
    path('classes/listagem/', lstcls),
    path('classe/<str:id>/', atzcls),
    path('classe/delete/<str:id>/', delcls),
    path('marcas/', brds),
    path('marcas/criacao/', crtbrd),
    path('marcas/listagem/', lstbrd),
    path('marca/<str:id>/', atzbrd),
    path('marca/delete/<str:id>/', delbrd),
    path('gestao/', gestao),
    path('gestao/criacao/', crtatv),
    path('gestao/listagem/', lstatv),
    path('gestao/<str:id>/', atzatv),
    path('gestao/delete/<str:id>/', delatv),
    path('pacotes/', pacotes),
    path('pacotes/criacao/', crtpkg),
    path('pacotes/listagem/', lstpkg),
    path('pacote/<str:id>/', atzpkg),
    path('pacote/gerenciamento/<str:id>/', mngpkg),
    path('pacote/delete/<str:id>/', delpkg),
    path('pacote/fechamento/<str:id>/', clspkg),
]
