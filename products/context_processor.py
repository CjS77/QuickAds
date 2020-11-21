from .models import Category, Product


def categories(request):
    all_cats = Category.objects.all()
    return {'all_categories': all_cats}


def all_products(request):
    all_products = Product.objects.order_by('created_at')
    return {'all_products': all_products}
