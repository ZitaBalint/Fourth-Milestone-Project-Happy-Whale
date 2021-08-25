from decimal import Decimal
from shop.models import Item


class Cart():

    def __init__(self, request):

        bag_items = []
        total = 0
        product_count = 0
        
        self.session = request.session
        cart = self.session.get('cart')

        if 'cart' not in request.session:
            cart = self.session['cart'] = {}
        self.cart = cart

    

