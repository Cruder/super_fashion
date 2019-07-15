from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import UploadFileForm


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            with open('public/' + request.FILES['file'].name, 'wb+') as destination:
                for chunk in request.FILES['file'].chunks():
                    destination.write(chunk)
            return HttpResponseRedirect('result')
    return HttpResponseRedirect('/fashion')


def result(request):
    template = loader.get_template('result.html')
    return HttpResponse(template.render({}, request))
