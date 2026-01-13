from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from .models import Movie
from .forms import MovieForm


class MovieMixin:
    model = Movie
    form_class = MovieForm
    template_name = 'movie/movie.html'
    success_url = reverse_lazy('movies:list')


class MovieCreateView(CreateView, MovieMixin):
    fields = '__all__'


class MovieUpdateView(UpdateView, MovieMixin):
    fields = '__all__'


class MovieDeleteView(DeleteView, MovieMixin):
    pass


class MovieListView(ListView):
    model = Movie
    ordering = 'id'
    paginate_by = 10
    template_name = 'movies/movies_list.html'
