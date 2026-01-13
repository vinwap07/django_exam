from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.MovieCreateView.as_view(), name='create'),
    # path('<int:movie_pk>/', ),
    path('update/<int:movie_pk>/',
         views.MovieUpdateView.as_view(), name='update'),
    path('delete/<int:movie_pk>/',
         views.MovieDeleteView.as_view(), name='delete'),
    path('list',
         views.MovieListView.as_view(), name='list')
]
