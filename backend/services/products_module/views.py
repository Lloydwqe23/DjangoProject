from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from services.products_module.models import Product, Currency
from services.products_module.forms import UpdateProductForm
from django.template.defaulttags import register
from django.contrib.auth.decorators import login_required
@register.filter
def get_range(value):
    return range(1, value + 1)
def index(request):
    products = Product.objects.all()
    paginator = Paginator(products, 1)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"products": page_obj, "pages_count": paginator.num_pages, 'page_number': page_number}
    return render(request, "index.html", context)

@login_required
def get_my_products(request):
    products = Product.objects.filter(owner=request.user)
    paginator = Paginator(products, 1)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"products": page_obj, "pages_count": paginator.num_pages, 'page_number': page_number}
    return render(request, "my_products.html", context)


def get_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "product.html", context={"product": product, "is_my_product": True})

@login_required
def create_product(request):
    if request.method == "POST":
        form = UpdateProductForm(request.POST)
        if form.is_valid():
            Currency.objects.first()
            product = Product.objects.create(title=form.data["title"],
                                             description=form.data["description"],
                                             price=form.data["price"],
                                             in_stock=True,
                                             owner=request.user,
                                             currency=Currency.objects.first())

            return redirect("product", pk=product.pk)
    else:
        form = UpdateProductForm()
    return render(request, "create_update_product.html", context={"form": form})


def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "create_update_product.html", context={"product": product, "is_my_product": True})


def delete_product(request, pk):
    get_object_or_404(Product, pk=pk).delete()
    return redirect("get_my_products")
