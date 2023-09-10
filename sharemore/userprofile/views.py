from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.contrib import messages

from .models import Userprofile
from store.forms import ItemForm
from store.models import Item

from core.context_processors import navigation

def vendor_page(request, pk):
    user = User.objects.get(pk=pk)
    items = user.items.all()
    
    context = {
        'user':user,
        'items': items,
    }
    
    return render(request, 'userprofile/vendor_detail.html', context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            
            user_profile = Userprofile.objects.create(user=user)
            
            return redirect('frontpage')
    else:
        form = UserCreationForm()
    return render(request, 'userprofile/signup.html',{
        'form': form
    })
    
@login_required
def myaccount(request):
    return render(request, 'userprofile/myaccount.html')


@login_required
def my_inventory(request):
    user = request.user
    items = request.user.items.exclude(is_deleted=True).all()
    
    context = {
     'items': items,
    }
    return render(request, 'userprofile/my_inventory.html', context)


@login_required
def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        
        if form.is_valid():
            item = form.save(commit=False)
            title = request.POST.get('title')

            item.user = request.user
            item.slug = slugify(title)
            item.save()
            
            messages.success(request, 'Item added!')
            
            return redirect('my_inventory')
    else:
        form = ItemForm()
        
        
    context = {
        'form': form,
         'title': 'Add Item',
         'add_update': 'Add',
    }
    return render(request, 'userprofile/add_item.html', context)

@login_required
def edit_item(request, pk):
    item = Item.objects.filter(user=request.user).get(pk=pk)
    
    if request.method == 'POST':
         form = ItemForm(request.POST or None, request.FILES or None, instance=item)
         if form.is_valid():
             item = form.save(commit=False)
             title = request.POST.get('title')
             item.slug = slugify(title)
             item.save()
             
             #http_response = HttpResponse()
             
             messages.success(request, 'Item updated successfully')
             
             return redirect('my_inventory')
    else:
        form = ItemForm(instance=item)
            
    context = {
        'form': form,
        'item': item,
        'title': 'Edit Item',
        'add_update': 'Update',

    }
    return render(request, 'userprofile/add_item.html', context)

@login_required
def delete_item(request, pk):
    item = Item.objects.filter(user=request.user).get(pk=pk)
    item.is_deleted = True
    item.save()
    messages.success(request, 'Item was deleted')
    
    return redirect('my_inventory')