import django_filters
from .models import Post, Sphere


class OrderFilter(django_filters.FilterSet):
    sphere = django_filters.ModelChoiceFilter(
        field_name='sphere',
        queryset=Sphere.objects.all(),
    )

    class Meta:
        model = Post
        fields = {'age': ['gte', 'lte']
        }
