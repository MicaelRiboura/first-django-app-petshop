from django.db import models


class templateModel(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name

class pet(models.Model):
	nome = models.CharField(max_length=255)
	tipo = models.CharField(max_length=20)
	image = models.ImageField(upload_to='static/images/', null=True)
	nascimento = models.DateField()
	def __str__(self):
		return 'Nome: ' + self.nome + ' - ' + self.tipo

# Model Field Reference: https://docs.djangoproject.com/en/3.0/ref/models/fields/

# Linha de texto:	models.CharField(max_length=XXX)
# Sim / Não:		models.BooleanField()
# Campos de Texto:	models.TextField()
# Imagens:			models.ImageField(upload_to='static/uploads')
# Arquivos:			models.FileField(upload_to='static/uploads')
# Relacionamento:	models.ForeignKey(NOME_MODELO, on_delete=PROTECT)
