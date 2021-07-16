from django import forms
from django.forms import widgets
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'body')

        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your post Title'}),
            'title_tag' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your post Title Tag'}),
            'author' : forms.Select(attrs={'class': 'form-control'}),
            'body' : forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Start Writing.. '}),

        }