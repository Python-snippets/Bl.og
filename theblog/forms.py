from django import forms
from django.forms import widgets
from .models import Post, Category, Comment

choices = Category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body', 'header_image')

        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your post Title'}),
            'title_tag' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your post Title Tag'}),
            'author' : forms.TextInput(attrs={'class': 'form-control', 'value': '',  'id':'dadmin', 'type':'hidden'}),
            #'author' : forms.Select(attrs={'class': 'form-control'}),
            'category' : forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body' : forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Start Writing.. '}),

        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')

        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your post Title'}),
            'title_tag' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your post Title Tag'}),
            #'author' : forms.Select(attrs={'class': 'form-control'}),
            'body' : forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Start Writing.. '}),

        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']