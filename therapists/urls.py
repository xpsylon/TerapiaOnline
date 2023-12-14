from django.urls import path
from . import views

app_name = 'therapists'

urlpatterns = [
    path('therapists/', views.therapist_list, name='therapist_list'), 
    path('therapists/<int:therapist_id>/', views.therapist_detail, name='therapist_detail'),
]
