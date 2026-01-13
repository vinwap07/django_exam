from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.ReviewCreateView.as_view(), name='create'),
    # path('<int:review_pk>/', ),
    path('update/<int:review_pk>/',
         views.ReviewUpdateView.as_view(), name='update'),
    path('delete/<int:review_pk>/',
         views.ReviewDeleteView.as_view(), name='delete'),
    path('list',
         views.ReviewListView.as_view(), name='list')
]
