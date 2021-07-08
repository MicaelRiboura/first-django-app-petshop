from django import forms

class templateForm(forms.Form):
	name = forms.CharField(max_length=100)

class formPet(forms.Form):
	nome = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}))
	tipo = forms.CharField(max_length=255,required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tipo'}))
	nascimento = forms.DateField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}))
	image = forms.ImageField()

# Form Field Reference: https://docs.djangoproject.com/en/3.0/ref/forms/fields/

# forms.CharField(max_length=XXX, required=False|True, label='NNNN')
# forms.ModelChoiceField(queryset=XXXX.order_by('XXXX'), empty_label='NNNNN', required=False|True,label='NNNN')
# forms.ImageField()
# forms.FileField()
# forms.BooleanField()

