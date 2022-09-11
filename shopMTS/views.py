from django.db.models import Q
from django.views.generic import ListView, DetailView
from .models import Product


class ListObjectsView(ListView):
    model = Product
    template_name = "main.html"
    context_object_name = "products"


class DetailObjectsView(DetailView):
    model = Product
    template_name = "detail.html"
    context_object_name = "product"


class SearchResultsView(ListView):
    model = Product
    template_name = 'searchresults.html'
    context_object_name = "product"

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Product.objects.filter(Q(name__icontains=query))
        return object_list
