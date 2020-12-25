from django import forms
from .models import Post, Sphere

choices = Sphere.objects.all().values_list('name', 'name')

choices_list = []

for item in choices:
    choices_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

        widgets = {
            'author_id': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'username', 'type': 'hidden'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'speciality': forms.TextInput(attrs={'class': 'form-control'}),
            'sphere': forms.Select(choices=choices_list, attrs={'class': 'form-control'}),
            'resume': forms.Textarea(attrs={'class': 'form-control'})
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('resume',)

        widgets = {
            'resume': forms.Textarea(attrs={'class': 'form-control'})
        }
