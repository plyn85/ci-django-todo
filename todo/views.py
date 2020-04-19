from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm
# Create your views here.


def get_todo_list(request):
    results = Item.objects.all()
    context = {'items': results}
    return render(request, "todo_list.html", context)


def create_an_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        # save to the database
        if form.is_valid():
            form.save()

        return redirect(get_todo_list)
#  else If the request is not a post
    else:
        form = ItemForm()
        context = {'form': form}
        return render(request, "item_form.html", context)


def edit_an_item(request, id):
    # pk is primary key witha value equal the Id
    item = get_object_or_404(Item, pk=id)
    if request.method == "POST":
        # if form == item from then we popualte we item we defined on line 29
        form = ItemForm(request.POST, instance=item)
        # sever side form validation
        if form.is_valid():
            # save the form
            form.save()
        return redirect(get_todo_list)
        # passing in the item as the instance that we want to contstruct the object from item is the entire feild from Item in inital.py
    else:
        # we just create an new form based of the Instace of that item
        form = ItemForm(instance=item)
        context = {'form': form}
    return render(request, "item_form.html", context)


def toggle_status(request, id):
    item = get_object_or_404(Item, pk=id)
    item.done = not item.done
    item.save()
    return redirect(get_todo_list)


def delete_an_item(request, id):
    item = get_object_or_404(Item, pk=id)
    form = ItemForm(request.POST, instance=item)
    item.delete()
    return redirect(get_todo_list)
