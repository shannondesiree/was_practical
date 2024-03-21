from django.shortcuts import render
from cats.models import Cat, Student


# Create your views here.
def index(request):
    students = Student.objects.order_by('last_name')
    cats = Cat.objects.order_by('name')
    context = {
        'students': students,
        'cats': cats,
    }
    return render(request, 'cats/index.html', context=context)

def pets(request):
    cats = Cat.objects.order_by('name')
    context = {
        'cats': cats,
    }
    return render(request, 'cats/pets.html', context=context)