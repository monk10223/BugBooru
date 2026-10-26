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
        labels = {'author': 'Name', 'text': 'Message'}
        error_messages = {
            'text': {'required': 'Write a message.'},
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].required = False

    def clean_author(self):
        return self.cleaned_data['author'].strip() or 'Anonymous'


class CommentEditForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'author']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].disabled = True