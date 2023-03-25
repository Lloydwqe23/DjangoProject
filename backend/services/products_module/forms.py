from django import forms
from services.products_module.models import Product

class UpdateProductForm(forms.ModelForm):
    #currency_id = forms.IntegerField()
    class Meta:
        model = Product
        #fields = ('title', 'description', 'price', 'currency_id', 'in_stock')
        fields = ('title', 'description', 'price', 'in_stock')
