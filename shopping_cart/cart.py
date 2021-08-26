from decimal import Decimal
from shop.models import Item


class Cart():

    def __init__(self, request):
        
        self.session = request.session
        cart = self.session.get('cart')

        if 'cart' not in request.session:
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self, item, quantity, size):

        item_id = item.id

        if item_id in self.cart:
            self.cart[item_id]['quantity'] = quantity
            self.cart[item_id]['size'] = size

        else:
            self.cart[item_id] = {
                'price': item.price,
                'quantity': quantity,
                'size': size
            }
        self.save()
  
    def save(self):
        self.session.modified = True
