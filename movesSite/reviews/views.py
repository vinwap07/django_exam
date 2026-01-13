from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from .models import Review
from .forms import ReviewForm


class ReviewMixin:
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review.html'
    success_url = reverse_lazy('reviews:list')


class ReviewCreateView(CreateView, ReviewMixin):
    fields = '__all__'


class ReviewUpdateView(UpdateView, ReviewMixin):
    fields = '__all__'


class ReviewDeleteView(DeleteView, ReviewMixin):
    pass


class ReviewListView(ListView):
    model = Review
    ordering = 'id'
    paginate_by = 10
