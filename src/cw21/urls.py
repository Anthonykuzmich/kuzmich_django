from django.urls import path
from .views import home, add_student

urlpatterns = [
    path('home', home, name='home'),
    path('add_student', add_student, name='add_student')
]
