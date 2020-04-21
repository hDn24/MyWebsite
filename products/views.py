from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
# Create your views here.
class AddNewProduct(LoginRequiredMixin, View):
    login_url = "/"

    def get(self, request):
        category = Category.objects.all()
        context = {
            "category": category,
        }
        return render(request, "products/addNewProduct.html", context)
