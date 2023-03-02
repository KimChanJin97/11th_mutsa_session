from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content']
        # fields = ['__all__']

# make class by inheriting class 'ModelForm'
class BlogForm1(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content']

# make metaclass 'BlogFormMeta1', which makes class 'BlogForm2'
BlogFormMetaClass = type('BlogFormMetaClass',
                (forms.ModelForm,),
                {'Meta': type('Meta',
                              (),
                              {'model': Blog, 'fields': ['title', 'content']})})

class BlogForm2(metaclass=BlogFormMetaClass):
    class Meta:
        model = Blog
        fields = ['title', 'content']
