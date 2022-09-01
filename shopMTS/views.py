from django.views.generic import ListView
# from .models import Users, Products
from .models import Product


class ListObjectsView(ListView):
    model = Product
    template_name = "main.html"
    context_object_name = "products"