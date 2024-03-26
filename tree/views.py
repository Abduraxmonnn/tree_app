from collections import defaultdict

from django.http import Http404
from django.shortcuts import render

from .models import Tree


def tree_list(request):
    items = Tree.objects.select_related('category').all()

    # Organize items by category
    items_by_category = defaultdict(list)
    for item in items:
        items_by_category[item.category].append(item)

    context = {
        'items_by_category': items_by_category.items()
    }

    return render(request, 'items/tree_list.html', context)


def tree_detail(request, name):
    try:
        item = Tree.objects.select_related('category').get(name=name)
    except Tree.DoesNotExist:
        return Http404

    context = {
        'item': item,
    }
    return render(request, 'items/tree_detail.html', context)
