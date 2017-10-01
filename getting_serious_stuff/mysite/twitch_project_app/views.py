from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.template.loader import get_template



def index(request):
    return render(request, 'index.html')


#template = get_template('index.html')
#html = template.render({'name': 'world'})