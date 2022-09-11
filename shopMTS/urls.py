from django.urls import path
from .views import ListObjectsView, DetailObjectsView, SearchResultsView

urlpatterns = [
    path('', ListObjectsView.as_view()),
    path('<int:pk>', DetailObjectsView.as_view(), name='detail'),
    path('search/', SearchResultsView.as_view(), name='search_results'),

    ]
