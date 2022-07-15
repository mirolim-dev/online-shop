from tkinter.messagebox import NO
from orders.models import WishlistModel, CartModel, Order
from profile_pages.models import UserInfo, UserAddress
from products.models import CategoryModel

def universal_objects(request):
    if request.user.is_authenticated:
        wishlist__objects = WishlistModel.objects.filter(user=request.user)
        cart__objects = CartModel.objects.filter(user=request.user)
        orders = Order.objects.filter(user=request.user)
        context = {
            'wishlist_items_count': wishlist__objects.count(),
            'cart_items_count': cart__objects.count(),
            'orders_count': orders.count()
        }
        return context
    return {}
   
   
def check_user_informations(request):
    if request.user.is_authenticated:
        alert_message = ""
        username = str(request.user.username)
        # print(f"username: {username}")
        
        try:
            user_informations = UserInfo.objects.filter(username=username)
        except:
            user_informations = None
        
        try:
            user_adresses = UserAddress.objects.filter(user=request.user).get(is_active=True)
        except:
            user_adresses = None
            
        if user_informations == None:
            alert_message += "User Informations Doesn't exist ! \n\tIf you wont to use our web\
                site's extra functions you should write information about yourself which\
                    is requested in profile settings page\n"
        
        if user_adresses == None:
            alert_message += "User address doesn't exists! \n\tIf you wont to order some items firts of all you should add your address "
        
        return {'alert_message': alert_message}
    
    return {}
        
        

def get_all_categories(request):
    categories = CategoryModel.objects.all().order_by("-last_added")
    print("CAtegories: ", categories)