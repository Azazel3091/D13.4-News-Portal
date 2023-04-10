from django import forms
from .models import Post
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):
    title = forms.CharField(min_length=10)

    class Meta:
       model = Post
       fields = [ 'author', 'categoryType', 'postCategory', 'title', 'text', 'rating', ]


       def clean_name(self):
           name = self.cleaned_data["name"]
           if name[0].islower():
               raise ValidationError(
                   "Название должно начинаться с заглавной буквы"
               )
           return name