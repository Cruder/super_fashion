from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
import matplotlib.image as img
import numpy as np
import tensorflow as tf
from keras.models import load_model
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
                ary = np.reshape(image, 28 * 28)
                print(len(ary))
                print(ary)
                model = tf.keras.models.load_model('fashion/trained_models/mlp_1_2.h5')
                print(model.predict(ary))
                FashionFile(file_name=file.name, type='2').save()
            process(x)
        return HttpResponseRedirect('result')
    return HttpResponseRedirect('/fashion')


def result(request):
    template = loader.get_template('result.html')
    files = FashionFile.objects.all()
    return HttpResponse(template.render({'files': files}, request))
