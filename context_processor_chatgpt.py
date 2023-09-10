@login_required
def my_inventory(request):
    user = request.user
    items = request.user.items.exclude(is_deleted=True).all()

    context = {
        'items': items,
    }

    # Ensure that 'items' from context processors do not overwrite your view's context
    context_data = dict(render(request, 'userprofile/my_inventory.html', {}).context_data, **context)
    return render(request, 'userprofile/my_inventory.html', context_data)
