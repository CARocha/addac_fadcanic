from selectable.base import ModelLookup
from selectable.registry import registry
from .models import Productores

class ProductorLookup(ModelLookup):
    model = Productores
    search_fields = ('nombre__icontains', )

registry.register(ProductorLookup)