from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
import matplotlib.image as img
import numpy as np
import tensorflow as tf
from keras.models import load_model
from .models import FashionFile, TrainedModel, Result
from .forms import UploadFileForm

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))


def upload_file(request):
    if request.method == 'POST':
        images = []
        fashion_files = []
        for count, file in enumerate(request.FILES.getlist("files")):
            with open('fashion/static/' + file.name, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            fashion = FashionFile(file_name=file.name)
            fashion.save()
            fashion_files.append(fashion)
            image = img.imread('fashion/static/' + file.name)
            images.append(np.reshape(image, 28 * 28))

        for trained_model in TrainedModel.objects.all():
            model = tf.keras.models.load_model('fashion/trained_models/' + trained_model.file_name)
            values = model.predict(np.array(images))
            for count, value in enumerate(values):
                final_id_value = np.argmax(value)
                Result(type=str(final_id_value), trained_model=trained_model, fashion_file=fashion_files[count]).save()

        return HttpResponseRedirect('result')
    return HttpResponseRedirect('/fashion')

def result(request):
    template = loader.get_template('result.html')
    files = FashionFile.objects.all()
    trained_models = TrainedModel.objects.all()
    results = list(Result.objects.all())
    dictionary = {}

    for result in results:
        file_name = model_from_id(files, result.fashion_file_id).file_name
        tuple = (
            result.get_type_display,
            model_from_id(trained_models, result.trained_model_id).name
        )
        if dictionary.get(file_name) is None:
            dictionary[file_name] = [tuple]
        else:
            dictionary[file_name].append(tuple)

    return HttpResponse(template.render({'results': dictionary}, request))

def model_from_id(models, id):
    for model in models:
        if model.id == id:
            return model
    return None

def models(request):
    template = loader.get_template('models.html')
    trained_models = TrainedModel.objects.all()
    return HttpResponse(template.render({'trained_models': trained_models}, request))

def upload_model(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            with open('fashion/trained_models/' + file.name, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            TrainedModel(file_name=file.name, name=form.cleaned_data["name"]).save()
    return HttpResponseRedirect('/fashion/models')
