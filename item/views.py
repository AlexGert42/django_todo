from django.shortcuts import render
from django.views.generic import ListView

from .models import Item


class HomePageTodo(ListView):
    model = Item
    template_name = 'item/index.html'
    context_object_name = 'content'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context = dict(list(context.items()))
        return context

    # def get_queryset(self):
    #     return Item.objects.filter(is_published=True).select_related('cat')

