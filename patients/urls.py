from django.urls import path
from . import views

urlpatterns = [
    path('', views.patient_list, name='patient_list'),
    path('patient/<int:id>/', views.patient_detail, name='patient_detail'),
    path('delete/<int:id>/', views.delete_patient, name='delete_patient'),
    path('edit/<int:id>/', views.edit_patient, name='edit_patient'),
]