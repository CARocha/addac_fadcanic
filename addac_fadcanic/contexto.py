from encuesta.forms import PrincipalForm

def globales(request):
	form = PrincipalForm(request.POST)
	return {'form':form}