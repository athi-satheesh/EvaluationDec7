from django.shortcuts import render, redirect

from new_app.models import Employee


# Create your views here.


def read(request):
    data = Employee.objects.all()
    return render(request, "index.html", {"data": data})


# delete-data
def delete(request, id):
    if request.method == 'POST':
        delt = Employee.objects.get(id=id)
        delt.delete()
        return redirect("read")
    return render(request, "index.html")
