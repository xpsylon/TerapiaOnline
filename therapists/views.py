from django.shortcuts import render, get_object_or_404
from .models import Therapist

def therapist_list(request):
    therapists = Therapist.objects.all()
    return render(request, 'therapists/therapist_list.html', {'terapeutas':therapists})

def therapist_detail(request, therapist_id):
    therapist = get_object_or_404(Therapist, id=therapist_id)
    return render(request, 'therapists/therapist_detail.html', {'terapeuta':therapist})