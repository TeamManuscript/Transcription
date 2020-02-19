from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from males.models import Male, Text
from .forms import MaleForm
from django.http import HttpResponseRedirect
import io
import os
from google.cloud import vision_v1p3beta1 as vision
from google.cloud.vision import types
from google.oauth2 import service_account
from google.cloud import storage
from google.protobuf import json_format
#credentials = service_account.Credentials.from_service_account_file(GCP_SERVICE_AUTH_FILE)

#credentials = service_account.Credentials.from_service_account_file(apikey.json)
#add api key here
#SERVICE = build(API, VERSION, developerkey=API_KEY)

def detect_text(path):
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)
    image_context = vision.types.ImageContext(
        language_hints=['en-t-i0-handwrit'])
    response = client.document_text_detection(image=image,
                                    image_context=image_context)
    texts = response.text_annotations
    for text in texts:
        return text.description.encode('utf-8')
        return text.description.language('en')



def detect_text_uri(uri):
    client = vision.ImageAnnotatorClient()
    image = vision.types.Image()
    image.source.image_uri = uri

    image_context = vision.types.ImageContext(
        language_hints=['en-t-i0-handwrit'])
    response = client.document_text_detection(image=image,
                                    image_context=image_context)
    texts = response.text_annotations
    print()
    for text in texts:
        print('\n"{}"'.format(text.description))
    print()


# 'https://img.etimg.com/photo/59421648/sarcasticrofl.jpg'


def main_home(request):
    form = MaleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        queryset = Male.objects.all()
        if len(queryset) >= 1:
            Male.objects.all().delete()
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect('response/')
    context = {
        "form": form,
    }
    return render(request, 'index.html', context)


def response(request):
    queryset = Male.objects.all()
    for each in queryset:
        res_text = detect_text(each.image.path)
        astring = res_text.decode().strip('\\n')
    context = {
        "object_list" : queryset,
        "restext": astring,
    }
    return render(request, 'result.html', context)

def save(request):
    if request.method == 'POST':
        # Gran inputs
        title = request.POST['title']
        texts = request.POST['text']

        if title and texts:
            data = Text(title=title, text=texts)
            data.save()
            success = 'scanned texts successful saved to the database'
            queryset = Male.objects.all()
            for each in queryset:
                res_text = detect_text(each.image.path)
                astring = res_text.decode().strip('\\n')
            context = {
                "object_list" : queryset,
                "restext": astring,
            }
            return render(request, 'result.html', context, {'success': success})
    else:
        return render(request, 'result.html')
