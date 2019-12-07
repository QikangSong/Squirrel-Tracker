from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    context = {"sightings": Sighting.objects.all().order_by('id'), "field_names": Sighting._meta.get_fields()}
    return render(request, 'sightings/index.html',context)
