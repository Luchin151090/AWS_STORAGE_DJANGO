from django.shortcuts import render
from django.views.generic.edit import FormView
from app1.models import Post
from app1.forms import Upload

# Create your views here.
class Upload(FormView):
    template_name = 'index.html'
    form_class = Upload
    success_url = '/'

    def form_valid(self,form):
        form.save()
        print(form.cleaned_data)
        return super().form_valid(form)