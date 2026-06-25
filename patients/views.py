from django.shortcuts import render
from .models import Patient

def patient_list(request):

    if request.method == "POST":
        Patient.objects.create(
            name=request.POST.get("name"),
            age=request.POST.get("age"),
            gender=request.POST.get("gender"),
            phone=request.POST.get("phone")
        )

    patients = Patient.objects.all()

    context = {
        "patients":patients,
        "total_patients": patients.count()
    }

    return render(
        request,
        "patients/patient_list.html",
        context
    )