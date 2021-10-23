from django import forms
from django.db.models import fields
from django.forms import ModelForm, widgets
from ckeditor.widgets import CKEditorWidget

from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['thumbnail', 'title', 'subtitle', 'content', 'private', 'tag']

        widgets = {
            'tag': forms.CheckboxSelectMultiple(),
        }

    