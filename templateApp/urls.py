from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [

	url(r'^pets/$', views.templateView, name="templateView"),
	url(r'^pet/register/$', views.insertPet, name="insertPet"),
	url(r'^pet/(?P<identificador>\w+)$', views.showDetail, name="showDetail"),
	url(r'^pet/delete/(?P<identificador>\w+)$', views.deletePet, name="deletePet"),
]

# URL com REGEX para buscar apenas um resultado
# url(r'^DETALHE/(?P<identificador>\w+)', views.DETALHE, name="DETALHE"),

# Parametro -> ?P
# Nome do parametro -> <identificador>
# Expressão regular para indicar o tipo -> \w+