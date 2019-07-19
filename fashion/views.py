from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
import matplotlib.image as img
from .models import FashionFile

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))


def upload_file(request):
    if request.method == 'POST':
        for count, x in enumerate(request.FILES.getlist("files")):
            def process(file):
                with open('fashion/static/' + file.name, 'wb+') as destination:
                    for chunk in file.chunks():
                        destination.write(chunk)
                image = img.imread('fashion/static/' + file.name)
                print(len(image))
                print(image)
                FashionFile(file_name=file.name, type='2').save()
            process(x)
        return HttpResponseRedirect('result')
    return HttpResponseRedirect('/fashion')


def result(request):
    template = loader.get_template('result.html')
    files = FashionFile.objects.all()
    return HttpResponse(template.render({'files': files}, request))
