from encuesta.forms import PrincipalForm

def globales(request):
	form_principal = PrincipalForm(request.POST)
	return {'form_principal':form_principal}