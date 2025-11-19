from django.forms import ModelForm
from .models import Kitob 

class KitobForm(ModelForm):
    class Meta:
        model = Kitob 
        fields = ["name", "description"]

        