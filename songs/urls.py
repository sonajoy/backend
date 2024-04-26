from django.urls import path
from . import views

urlpatterns = [
    path('songs/', views.SongListCreateView.as_view(), name='song-list-create'),
    path('songs/<int:pk>/', views.SongDetailView.as_view(), name='song-detail'),
    path('songs/update/<int:pk>/', views.SongUpdateView.as_view(), name='song-update'),

]

