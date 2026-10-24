from django import forms
from django.forms.models import ModelForm

from comments.models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'author']
        widgets = {
            'text': forms.Textarea(),
            'author': forms.TextInput()
        }
#TODO add error messages