from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from .models import Collection
from .forms import CollectionForm


class CollectionMixin:
    model = Collection
    form_class = CollectionForm
    template_name = 'collection/collection.html'
    success_url = reverse_lazy('collection:list')


class CollectionCreateView(CreateView, CollectionMixin):
    fields = '__all__'


class CollectionUpdateView(UpdateView, CollectionMixin):
    fields = '__all__'


class CollectionDeleteView(DeleteView, CollectionMixin):
    pass


class CollectionListView(ListView):
    model = Collection
    ordering = 'id'
    paginate_by = 10
