from django import forms
from .models import *

class PostForm(forms.ModelForm):

    class Meta:
        model = Pessoa
        fields = (
            'nome',
            'user_name',
            'email',
            'senha',
            'biografia'
        )