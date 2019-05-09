from django import forms
from .models import Comment2


class CommentForm2(forms.ModelForm):
    class Meta:
        model = Comment2
        fields = ('author', 'text')