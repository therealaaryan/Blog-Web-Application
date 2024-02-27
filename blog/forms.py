from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'text')
        labels = {
            'title' : 'Your Blog Title (limit it upto 300 characters)',
            'text' : 'Your Blog'
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'text': forms.Textarea(attrs={'class': 'form-control mb-5'})
        }
