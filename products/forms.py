from django import forms


class AddProductForm(forms.Form):
    name = forms.CharField(max_length=500, required=True)
    describe = forms.CharField(max_length=500, required=False)
    content = forms.CharField(max_length=1000, required=False)
    available = forms.IntegerField(min_value=0)
    price = forms.IntegerField(min_value=0, required=False)
    discount = forms.IntegerField(min_value=0, max_value=100, required=False)
    mainPicture = forms.ImageField(required=False)
    pictures = forms.ImageField(widget=forms.ClearableFileInput(attrs={"multiple": True}), required=False)

