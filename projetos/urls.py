
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


from . import views

app_name = "projetos"

urlpatterns = [
    # ex: /projetos/
    path("", views.index, name="index"),

        # ex: /projetos/
    path("projetos", views.projetos, name="projetos"),

    # ex: /projetos/3/
    path("<int:id>/", views.detalhe, name="detalhe"),

        # ex: /projetos/3/
    path("<int:id>/edit", views.edit, name="edit"),

           # ex: /projetos/3/
    path("<int:id>/editar", views.projeto_update, name="editar"),

            # ex: /projetos/3/
    path("<int:id>/deletar", views.deletar, name="deletar"),

                # ex: /projetos/3/
    path("novo", views.novo, name="novo"),

    path("adicionar", views.adicionar, name="adicionar"),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)