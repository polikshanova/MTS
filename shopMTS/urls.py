from django.urls import path
from .views import ListObjectsView

urlpatterns = [
    path('', ListObjectsView.as_view()),
    ]
