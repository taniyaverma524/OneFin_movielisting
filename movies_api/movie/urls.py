from django.urls import path
from movie.views import *

app_name = 'movie'

urlpatterns = [
    path('movies/',GetMoviesView.as_view(),name='get_movieslist'),
    path('collections/',MovieCollectionView.as_view(),name='create_collection'),
    path('collections/<str:pk>/',MovieCollectionView.as_view(),name='update_collection'),

]