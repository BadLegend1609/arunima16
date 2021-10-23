from django.db.models import query
from django.db.models.query import QuerySet
import django_filters
from django_filters import CharFilter

from django import forms
from .models import *

class PostFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains', label='Title: ')
    tag = django_filters.ModelChoiceFilter(queryset=Tag.objects.all(),
        widget = forms.CheckboxSelectMultiple,
        label='Tags: '
    )
    class Meta:
        model = Post
        fields = ['title', 'tag']