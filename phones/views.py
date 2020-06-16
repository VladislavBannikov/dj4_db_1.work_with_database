from django.shortcuts import render
from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'

    sort_type = request.GET.get("sort", None)
    phones = Phone.objects.values("name", "price", "image", "slug")
    if sort_type:
        if sort_type == "name":
            phones = phones.order_by("name")
        elif sort_type == "max_price":
            phones = phones.order_by("-price")
        elif sort_type == "min_price":
            phones = phones.order_by("price")

    context = {"phones": phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {"phone": Phone.objects.get(slug=slug)}
    return render(request, template, context)
