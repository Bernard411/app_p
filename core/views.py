# diagnosis/views.py
from django.shortcuts import render

from .models import Disease
# core/views.py

from django.shortcuts import render
from .forms import PlantDiagnosisForm
from .models import Disease

def home(request):
    diagnosis_result = None

    if request.method == 'POST':
        form = PlantDiagnosisForm(request.POST)
        if form.is_valid():
            # Extract form data
            leaf_color = form.cleaned_data['leaf_color']
            leaf_shape = form.cleaned_data['leaf_shape']
            spots_on_leaves = form.cleaned_data['spots_on_leaves']
            wilting = form.cleaned_data['wilting']
            mold_growth = form.cleaned_data['mold_growth']
            stem_condition = form.cleaned_data['stem_condition']

            # Simple diagnostic rules - these should be expanded
            if leaf_color == "yellow" and spots_on_leaves:
                diagnosis_result = Disease.objects.filter(name="Leaf Spot Disease").first()
            elif wilting and mold_growth:
                diagnosis_result = Disease.objects.filter(name="Blight").first()
            elif leaf_color == "yellow" and stem_condition == "soft":
                diagnosis_result = Disease.objects.filter(name="Root Rot").first()
            # Add more diagnostic rules here

    else:
        form = PlantDiagnosisForm()

    return render(request, 'index.html', {
        'form': form,
        'diagnosis_result': diagnosis_result
    })



from django.shortcuts import render
from .dl_model.model import classify_image
from django.core.files.storage import FileSystemStorage


# Create your views here.
def datasets(request):
    if request.method == "GET":
        return render(request, 'vision.html')
    if request.method == 'POST':
        # Access the input (image) stream and keep it in the Filestorage
        unploaded_file = request.FILES['myfile']
        #convert the file to bytes
        image = unploaded_file.read()
        # predict the class of the image
        result = classify_image(image)
        #Select the top three predictions according to their probabilities
        top1 = '1. Species: %s, Status: %s, Probability: %.4f'%(result[0][0], result[0][1], result[0][2])
        top2 = '2. Species: %s, Status: %s, Probability: %.4f'%(result[1][0], result[1][1], result[1][2])
        top3 = '3. Species: %s, Status: %s, Probability: %.4f'%(result[2][0], result[2][1], result[2][2])

        predictions = [ { 'pred':top1 }, { 'pred':top2 }, { 'pred':top3 } ]
        context = { 'predictions':predictions }

        # ## In addition to image classification, Let's store the predicted filecd
        # # Save the file to ./media
        fs = FileSystemStorage()
        filename = fs.save(unploaded_file.name, unploaded_file)
        uploaded_file_url = fs.url(filename)
        context['url'] = uploaded_file_url

        return render(request, 'vision.html', context)
  

from django.shortcuts import render
from .forms import PlantDiagnosisForm
from .utils import diagnose_plant

def intel(request):
    diagnosis_result = None
    recommendations = None

    if request.method == 'POST':
        form = PlantDiagnosisForm(request.POST)
        if form.is_valid():
            # Extract form data
            leaf_color = form.cleaned_data['leaf_color']
            leaf_shape = form.cleaned_data['leaf_shape']
            spots_on_leaves = form.cleaned_data['spots_on_leaves']
            wilting = form.cleaned_data['wilting']
            mold_growth = form.cleaned_data['mold_growth']
            stem_condition = form.cleaned_data['stem_condition']
            soil_type = form.cleaned_data['soil_type']
            weather_conditions = form.cleaned_data['weather_conditions']
            watering_frequency = form.cleaned_data['watering_frequency']
            pest_presence = form.cleaned_data['pest_presence']
            fertilizer_use = form.cleaned_data['fertilizer_use']

            # Use the diagnose_plant function from utils.py
            diagnosis_result, recommendations = diagnose_plant(
                leaf_color, leaf_shape, spots_on_leaves, wilting,
                mold_growth, stem_condition, soil_type, weather_conditions,
                watering_frequency, pest_presence, fertilizer_use
            )
    else:
        form = PlantDiagnosisForm()

    return render(request, 'forms.html', {
        'form': form,
        'diagnosis_result': diagnosis_result,
        'recommendations': recommendations,
    })

def plant_bot(request):
    return render(request, 'bot.html')

def predict(request):
    if request.method == "GET":
        return render(request, 'vision.html')
    if request.method == 'POST':
        # Access the input (image) stream and keep it in the Filestorage
        unploaded_file = request.FILES['myfile']
        #convert the file to bytes
        image = unploaded_file.read()
        # predict the class of the image
        result = classify_image(image)
        #Select the top three predictions according to their probabilities
        top1 = '1. Species: %s, Status: %s, Probability: %.4f'%(result[0][0], result[0][1], result[0][2])
        top2 = '2. Species: %s, Status: %s, Probability: %.4f'%(result[1][0], result[1][1], result[1][2])
        top3 = '3. Species: %s, Status: %s, Probability: %.4f'%(result[2][0], result[2][1], result[2][2])

        predictions = [ { 'pred':top1 }, { 'pred':top2 }, { 'pred':top3 } ]
        context = { 'predictions':predictions }

        # ## In addition to image classification, Let's store the predicted filecd
        # # Save the file to ./media
        fs = FileSystemStorage()
        filename = fs.save(unploaded_file.name, unploaded_file)
        uploaded_file_url = fs.url(filename)
        context['url'] = uploaded_file_url

        return render(request, 'vision.html', context)
    

def application(request):
    plant = Disease.objects.all()
    context = {
        'plant':plant,
    }
    return render(request, 'try.html', context)

def view_d(request, pk):
    plant = Disease.objects.all()
    data = Disease.objects.get(pk=pk)
    context = {
        'data' : data,
        'plant': plant
    }
    
    return render(request, 'view.html', context)

def bot(request):
    return render(request, 'bot.html')

def scan(request):
    diagnosis_result = None

    if request.method == 'POST':
        form = PlantDiagnosisForm(request.POST)
        if form.is_valid():
            # Extract form data
            leaf_color = form.cleaned_data['leaf_color']
            leaf_shape = form.cleaned_data['leaf_shape']
            spots_on_leaves = form.cleaned_data['spots_on_leaves']
            wilting = form.cleaned_data['wilting']
            mold_growth = form.cleaned_data['mold_growth']
            stem_condition = form.cleaned_data['stem_condition']

            # Simple diagnostic rules - these should be expanded
            if leaf_color == "yellow" and spots_on_leaves:
                diagnosis_result = Disease.objects.filter(name="Leaf Spot Disease").first()
            elif wilting and mold_growth:
                diagnosis_result = Disease.objects.filter(name="Blight").first()
            elif leaf_color == "yellow" and stem_condition == "soft":
                diagnosis_result = Disease.objects.filter(name="Root Rot").first()
            # Add more diagnostic rules here

    else:
        form = PlantDiagnosisForm()

    return render(request, 'scan.html', {
        'form': form,
        'diagnosis_result': diagnosis_result
    })
