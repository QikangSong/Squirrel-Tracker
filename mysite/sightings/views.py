from django.shortcuts import render
from django.http import HttpResponse
# Create your views here
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import ModelForm
import random
from django.db.models import Sum, Count

from .models import Sighting

class SightingForm(ModelForm):
    class Meta:
        model = Sighting
        fields = '__all__'

def sighting_list(request):
    template='sightings/list.html'
    sightings = Sighting.objects.all()
    context = {
            'sightings' : sightings,
    }
    return render(request, template, context)


def sighting_add(request):
    template='sightings/add.html'
    form = SightingForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(reverse('sighting_list'))
    return render(request, template, {'form':form})

def sighting_update(request, squirrel_id):
    template='sightings/update.html'
    sighting = get_object_or_404(Sighting, pk=squirrel_id)
    form = SightingForm(request.POST or None, instance=sighting)
    if request.method=='POST' and 'update' in request.POST:
        if form.is_valid():
            form.save()
            return redirect(reverse('sighting_list'))
    return render(request, template, {'form':form})

def sighting_stats(request):
    template = 'sightings/stats.html'
    stats_list = [
            Sighting.objects.aggregate(total_squirrels_number = Count('squirrel_id')),
            Sighting.objects.filter(age ='Adult').aggregate(num_Adult_number = Count('squirrel_id')),
            Sighting.objects.filter(age ='Juvenile').aggregate(num_Juvenile_Squirrels = Count('squirrel_id')),
            Sighting.objects.filter(fur_color='Gray').aggregate(color_Gray_Squirrels_number = Count('squirrel_id')),
            Sighting.objects.filter(running ='True').aggregate(running_True_Squirrels_number = Count('squirrel_id')),
            ]
    sighting_list=[]
    for sighting in stats_list:
        sighting_list.append([list(sighting.keys())[0],list(sighting.values())[0]])
    context = {'stats':sighting_list,}
    return render(request, template, context)
