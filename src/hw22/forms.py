from .models import MusicBand
from django.forms import ModelForm, TextInput


class BandForm(ModelForm):
    class Meta:
        model = MusicBand
        fields = '__all__'
