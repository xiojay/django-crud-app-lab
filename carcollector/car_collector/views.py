from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Car, Modification, Tag
from .forms import CarForm, ModificationForm, TagForm 


def home(request):
    return render(request, 'home.html')

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'car_list.html', {'cars': cars})

def car_create(request):
    if request.method == "POST":
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('car_list')
    else:
        form = CarForm()
    return render(request, 'car_form.html', {'form': form})

@login_required
def car_update(request, car_id):
    car = get_object_or_404(Car, id=car_id)

    if request.method == "POST":
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('car_list')
    else:
        form = CarForm(instance=car) 

    return render(request, 'car_form.html', {'form': form}) 



def car_delete(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == "POST":
        car.delete()
        return redirect('car_list')
    return render(request, 'car_confirm_delete.html', {'car': car})


def mod_list(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    return render(request, 'mod_list.html', {'car': car})


def mod_create(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == "POST":
        form = ModificationForm(request.POST)
        if form.is_valid():
            mod = form.save(commit=False)
            mod.car = car
            mod.save()
            return redirect('mod_list', car_id=car.id)
    else:
        form = ModificationForm()
    return render(request, 'mod_form.html', {'form': form, 'car': car})

def mod_delete(request, mod_id):
    mod = get_object_or_404(Modification, id=mod_id)
    car_id = mod.car.id
    if request.method == "POST":
        mod.delete()
        return redirect('mod_list', car_id=car_id)
    return render(request, 'mod_confirm_delete.html', {'mod': mod})

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect('car_list')  
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def car_create(request):
    if request.method == "POST":
        form = CarForm(request.POST)
        if form.is_valid():
            car = form.save(commit=False)
            car.save()
            return redirect('car_list')  
    else:
        form = CarForm()
    return render(request, 'car_form.html', {'form': form})

@login_required
def car_update(request, car_id):
    car = get_object_or_404(Car, id=car_id)

    form = CarForm(instance=car)  

    if request.method == "POST":
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('car_list')

    return render(request, 'car_form.html', {'form': form})  


@login_required
def car_delete(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == "POST":
        car.delete()
        return redirect('car_list') 
    return render(request, 'car_confirm_delete.html', {'car': car})


@login_required
def mod_create(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == "POST":
        form = ModificationForm(request.POST)
        if form.is_valid():
            mod = form.save(commit=False)
            mod.car = car  
            mod.save()
            return redirect('mod_list', car_id=car.id)  
    else:
        form = ModificationForm()
    return render(request, 'mod_form.html', {'form': form, 'car': car})


@login_required
def mod_delete(request, mod_id):
    mod = get_object_or_404(Modification, id=mod_id)
    car_id = mod.car.id
    if request.method == "POST":
        mod.delete()
        return redirect('mod_list', car_id=car_id) 
    return render(request, 'mod_confirm_delete.html', {'mod': mod})

@login_required
def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'tag_list.html', {'tags': tags})

@login_required
def tag_create(request):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tag_list')
    else:
        form = TagForm()
    return render(request, 'tag_form.html', {'form': form})