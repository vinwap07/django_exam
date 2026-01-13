from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CollectionCreateView.as_view(), name='create'),
    # path('<int:collection_pk>/', views.GetCollection(), name='collection'),
    path('update/<int:collection_pk>/',
         views.UpdateView.as_view(), name='update'),
    path('delete/<int:collection_pk>/',
         views.DeleteView.as_view(), name='delete'),
    path('list', views.CollectionListView.as_view(), name='list')
]
