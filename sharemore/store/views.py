from django.shortcuts import render, get_object_or_404
from django.db.models import Q


from .models import Item, Category

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    items = category.items.exclude(is_deleted=True).all()
    
    context =  {
        'category': category,
        'items': items,
    }
    
    return render(request, 'store/category_detail.html', context)

def item_detail(request, category_slug, slug):
    item = get_object_or_404(Item,slug=slug, is_deleted=False)
    context = {
        'item': item,
    }
    return render(request, 'store/item_detail.html', context)

def search(request):
    query = request.GET.get('query', '')
    items = Item.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
    context = {
        'query': query,
        'items': items,
    }
    return render(request, 'store/search.html', context)