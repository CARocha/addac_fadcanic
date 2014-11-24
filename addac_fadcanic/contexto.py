from encuesta.forms import PrincipalForm
from django.contrib.auth.forms import AuthenticationForm

def globales(request):
	form_principal = PrincipalForm(request.POST)
	form1 = AuthenticationForm()
	return {'form_principal':form_principal, 'form1':form1}