from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload_file', views.upload_file),
    path('upload_model', views.upload_model),
    path('result', views.result),
    path('models', views.models),
]
