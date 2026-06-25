from django.shortcuts import render,redirect
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

def patient_detail(request, id):
    patient = Patient.objects.get(id=id)

    return render(
        request,
        'patients/patient_detail.html',
        {'patient': patient}
    )

def delete_patient(request, id):
    patient = Patient.objects.get(id=id)
    patient.delete()

    return redirect('patient_list')

def edit_patient(request, id):
    patient = Patient.objects.get(id=id)

    if request.method == 'POST':
        patient.name = request.POST['name']
        patient.age = request.POST['age']
        patient.gender = request.POST['gender']
        patient.phone = request.POST['phone']

        patient.save()

        return redirect('patient_list')

    return render(
        request,
        'patients/edit_patient.html',
        {'patient': patient}
    )


