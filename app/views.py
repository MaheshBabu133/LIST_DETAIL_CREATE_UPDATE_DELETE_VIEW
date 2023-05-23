from django.shortcuts import render

from app.models import *
from django.http import HttpResponse
# Create your views here.
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView

#iam defining this method to collect the data from the url
def get_url(request,na):
    return HttpResponse(f'<h1>{na} is my traier,and {na} is very good talented</h1>')
    #http://127.0.0.1:8000/get_url/harshad search url like this then you get
    #output:
    #harshad is my traier,and harshad is very good talented





class home(TemplateView):
    template_name='app/home.html'





#if we mention templatenames as following pattern then automatically it will render the html page
#you no need to mension the template_name directly the django will takes the place

#modelname_list.html------------->The class is inherited from ListView

#modelname_detail.html------------->The class is inherited from DetailView

#modelname_form.html------------->The class is inherited from CreateView or UpdateeView

#modelname_confime_delete.html------------->The class is inherited from DeleteView



class school_list(ListView):
    #template_name='app/school_list.html'
    model = School
    context_object_name='schools'
    ordering='name'

class SchoolDetail(DetailView):
    #template_name = "app/school_detail.html"
    model = School
    context_object_name='sclobj'
    ordering='sname'


