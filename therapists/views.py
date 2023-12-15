from django.shortcuts import render
from .models import Therapist

def therapist_list(request):
    therapists = Therapist.objects.all()
    return render(request, 'therapists/therapist_list.html', {'terapeutas':therapists})

def therapist_detail(request):
    therapist = Therapist.objects.get(id=therapist.id)
    return render(request, 'therapist_detail.html', {'terapeuta':therapist})