from django import forms

from bloggapp.models import Blog

class BlogF(forms.ModelForm):
    class Meta:
        model=Blog
        fields=["title","name","created_on","description"]



#["title","name","created_on","description"]