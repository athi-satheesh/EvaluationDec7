from django.shortcuts import render, redirect

from new_app.forms import EmployeeForm
from new_app.models import Employee


# Create your views here.

# create-date
def create(request):
    form = EmployeeForm()
    if request.method == "POST":
        form1 = EmployeeForm(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect("")
        else:
            form = form1
    return render(request, "addEmployee.html", {"form": form})


# read-data
def read(request):
    data = Employee.objects.all()
    return render(request, "index.html", {"data": data})


# update-data
def update(request, id):
    emp = Employee.objects.get(id=id)
    form = EmployeeForm(instance=emp)
    if request.method == "POST":
        form1 = EmployeeForm(request.POST, instance=emp)
        if form1.is_valid():
            form1.save()
            return redirect("")
    return render(request, "updateEmployee.html", {'form': form})


# delete-data
def delete(request, id):
    if request.method == 'POST':
        delt = Employee.objects.get(id=id)
        delt.delete()
        return redirect("")
    return render(request, "index.html")
