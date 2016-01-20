from django import template
import locale
register = template.Library()

@register.filter(name='calculaperct')
def calculaperct(value1, value2):
    try:
        resultado = (float(value1) / value2 * 100)
        return resultado
    except:
        return 0

@register.filter(name='calculaIngreso')
def calculaIngreso(value1, value2):
    try:
        resultado = float(value1) * float(value2)
        return resultado
    except:
        return 0
