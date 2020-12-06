from .models import Student
from django.forms import ModelForm, TextInput


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'age', 'profession']
        widgets = {
            'first_name': TextInput(),
            'last_name': TextInput(),
            'age': TextInput(),
            'profession': TextInput()
        }
