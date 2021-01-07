from django import forms
from django.core.mail import send_mail

from .models import Post, Sphere

choices = Sphere.objects.all().values_list('name', 'name')

choices_list = []

for item in choices:
    choices_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'age', 'speciality', 'sphere', 'resume', 'image', 'cv_pdf')

        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'username', 'type': 'hidden'}),
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


class EmailForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField(label='E-Mail')
    subject = forms.CharField(required=False)
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']
        send_mail(subject, message, email, ['jemope4869@girtipo.com'], fail_silently=False)
        pass
