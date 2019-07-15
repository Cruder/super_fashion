from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import UploadFileForm
from .models import FashionFile

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            with open('fashion/static/' + file.name, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            FashionFile(file_name=file.name, type='anime').save()
            return HttpResponseRedirect('result')
    return HttpResponseRedirect('/fashion')


def result(request):
    template = loader.get_template('result.html')
    files = FashionFile.objects.all()
    return HttpResponse(template.render({'files': files}, request))
