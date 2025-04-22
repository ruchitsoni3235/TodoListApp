from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages


def home(request):
    form = ListForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Item has been added successfully into the list!!!')
            return redirect('home')

    all_items = List.objects.all()
    return render(request, "home.html", {'all_items': all_items, 'form': form})


def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, 'item has been deleted successfully!!')
    return redirect('home')


def cross_off(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('home')


def uncross(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('home')


def edit(request, list_id):
    item = List.objects.get(pk=list_id)

    if request.method == 'POST':
        form = ListForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item has been edited successfully')
            return redirect('home')
        else:
            return render(request, 'edit.html', {'item': item, 'form': form})
    else:
        form = ListForm(instance=item)
        return render(request, 'edit.html', {'item': item, 'form': form})
