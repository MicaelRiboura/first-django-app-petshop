from django.shortcuts import render
from .forms import templateForm, formPet
from .models import templateModel
from .models import pet
from django.contrib.auth.decorators import login_required


def templateView(request):
	lista_pets = pet.objects.all()

	return render(request, "templateApp/templateView.html", {'lista': lista_pets})

def showDetail(request, identificador = ''):
	pet_escolhido = pet.objects.get(id=identificador)
	return render(request, "templateApp/detailView.html", {'pet': pet_escolhido})

def insertPet(request):
	if request.POST:
		form = formPet(request.POST, request.FILES)
		if form.is_valid():
			petObject = pet()
			petObject.nome = form.cleaned_data['nome']
			petObject.tipo = form.cleaned_data['tipo']
			petObject.nascimento = form.cleaned_data['nascimento']
			petObject.image = form.cleaned_data['image']
			petObject.save()

	formulario = formPet()
	return render(request, "templateApp/insertPet.html", {'formulario': formulario})

@login_required
def deletePet(request, identificador):
	try:
		pet.objects.get(id=identificador).delete()
		lista_pets = pet.objects.all()
		return render(request, "templateApp/templateView.html", {'lista': lista_pets})
	except:
		return render(request, "templateApp/templateView.html", {'lista': lista_pets, })

# View para pegar identificador. Ver URLS
# def DETALHE(request, identificador = ''):

# None é o null do Python
# O None é qualquer valor que seja nulo, não aceito, e não a ausência de valor