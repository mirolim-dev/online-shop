from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from products import models

from orders.models import CartModel


# Create your views here.

@login_required(login_url='/register/login/')
def home_view(request):
    categories = models.CategoryModel.objects.all()
    subcategories = models.SubcategoryModel.objects.all()
    products = models.ProductModel.objects.all()
    for im in products:
        print(im.image.url)
    cart_objects = CartModel.objects.filter(user = request.user)
    
    # Popular category section
    k=0
    popular_category_list = []
    for c in categories:
        k += 1
        len_list = len(list(categories))
        popular_category_list.append(list(categories)[len_list-k])
        if k==3:
            break
    # ....................
    
    
    # category section which is nearby the deals and offers section
    r=0
    d_o_category_list = [] # deals_and_offers category
    for ce in categories:
        r += 1
        len_list = len(list(categories))
        d_o_category_list.append(list(categories)[len_list-r])
        if r==5:
            break
    # ....................
   
    # .......recommended products section
  
    list_zero = []                                  # ushbu amallarim orqali men subcategorylari birxil bolgan          
    t=0                                             # mahsulotlarni  cheklab o'tishga yani bitta subcategorydan faqat 1 ta mahsulotnigina
    recommended_products = []                       # olishga erishdim
    list_products = list(products)                     
    for i in products:                                  
        t += 1
        a = list_products[-t]
        ab = a.subcategory_slug
        
        if ab not in list_zero:
            recommended_products.append(a)
            ac=ab
            list_zero.append(ac)
            if t == 12 or t > len(list_products):
                break 
    # ................
    
    context = {
        'categories': categories,
        'subcategories': subcategories,
        'recommended_products': recommended_products,
        'popular_category': popular_category_list,
        'd_o_category': d_o_category_list,
        'cart_objects': cart_objects,
    }

    return render(request, 'index.html', context)


def blank_starter(request):
    
    return render(request, 'blank-starter.html')




def search_view(request):
    if request.POST:
        searched = request.POST["searched"]
        searched_products = models.ProductModel.objects.filter(name__contains=searched)
        context = {
            'searched_products': searched_products,
        }
    return render(request, "searched_page.html", context)