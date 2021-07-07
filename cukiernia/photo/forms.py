from django import forms
from .models import Photo

class PostForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'cover']