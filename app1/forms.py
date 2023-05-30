from django import forms
from app1.models import Post

class Upload(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo','image_caption','image',]

        widgets ={
            'titulo':forms.TextInput(attrs={'class':'form-control'}),
            'image_caption':forms.TextInput(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'mt-3 border-0'})
        }