from django.forms import ModelForm
from .models import Usuari

class PersonaFrom(ModelForm):
    class Meta:
        model = Usuari
        fields = ['id', 'nom', 'cognom', 'assignatures', 'rol']
        # fields = '__all__'