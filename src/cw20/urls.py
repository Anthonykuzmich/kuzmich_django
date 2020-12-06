from django.urls import path
from .views import form, erase

urlpatterns = [
    path('', form, name='form'),
    path('erase', erase, name='erase')
]
