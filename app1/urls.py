from django.urls import path
from app1.views import Upload

app_name = 'app1'

urlpatterns = [
    path('',Upload.as_view(),name='upload'),

]