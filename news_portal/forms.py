from django.db import models
from django import forms
from django.core.exceptions import ValidationError





class PostForm(forms.ModelForm):
   class Meta:
       model = Post
       fields = [
           'name',
           'description',
           'category'
       ]

       def clean(self):
           cleaned_data = super().clean()
           description = cleaned_data.get("description")
           if description is not None and len(description) < 20:
               raise ValidationError({
                   "description": "Текст не может быть менее 20 символов."
               })

       if name == description:
           raise ValidationError(
               "Текст не должен быть идентичен названию."
           )

           return cleaned_data