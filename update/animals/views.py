from django.shortcuts import render, redirect
from .models import Animals
from .forms import AnimalForm

# Create your views here.
def home(request):
    return render(request, 'animals/home.html')

def animals(request):
    animals = Animals.objects.all()
    return render(request, 'animals/animals.html', {'animals': animals})

def newAnimals(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AnimalForm()

    return render(request, 'animals/new-animal.html', {'form': form})

def animalDetails(request, id):
    animal = Animals.objects.get(id=id)
    return render(request, 'animals/animal-details.html', {'animal': animal})

def delete(request, id):
    animal = Animals.objects.get(id=id)
    animal.delete()
    return redirect('animals')

def update(request, id):
    animal = Animals.objects.get(id=id)
    if request.method == 'POST':
        form = AnimalForm(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('animals')
    else:
        form = AnimalForm(instance=animal)

    return render(request, 'animals/animal-edit.html', {'form': form})
