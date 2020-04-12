from django.urls import path
from .views import *

urlpatterns = [
    path("add-new/", AddNewProduct.as_view(), name="addNewProduct"),
]