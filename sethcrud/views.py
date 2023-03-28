from django.shortcuts import render, redirect
from .models import Person

def insertdata(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        contact = request.POST.get('contact')
        amount = request.POST.get('amount')

        query = Person(name=name, email=email, age=age, gender=gender,
                       contact=contact, amount=amount)
        query.save()
        return redirect("/")
    return render(request, "index.html")


def index(request):
    data = Person.objects.all
    context = {"data": data}
    return render(request, "index.html", context)

def deletedata(request, id):
    d = Person.objects.get(id=id)
    d.delete()
    return redirect("/")
    return render(request, "index.html")

def updatedata(request, id):
    d = Person.objects.get(id=id)
    return render(request, 'edit.html', {'d':d})
