from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *
# Create your views here.
class AddNewProduct(LoginRequiredMixin, View):
    login_url = "/"

    def get(self, request):
        category = Category.objects.all()
        context = {
            "category": category,
        }
        return render(request, "products/addNewProduct.html", context)

    def post(self, request):
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            print("OKKKKKKKKK")
            print(request.POST.getlist("category"))
            print(request.FILES.getlist('pictures'))
        else:
            print("Not ok")
        return redirect("/manage-product/add-new")
