
def filter_by_price(request, products):
    
    max_price = request.GET.get('min', None)
    min_price = request.GET.get('max', None)
    
    if min_price:
        products = products.filter(price__gte=min_price)
    
    if max_price:
        products = products.filter(price__gte=max_price)
    
    return products