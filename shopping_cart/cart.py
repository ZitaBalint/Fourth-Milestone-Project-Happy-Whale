from decimal import Decimal
from shop.models import Item


class Cart():

    """ 
    Creates a session cookie for cart
    """

    def __init__(self, request):
        
        self.session = request.session
        cart = self.session.get('cartkey')

        if 'cartkey' not in request.session:
            cart = self.session['cartkey'] = {}
        self.cart = cart

    def add(self, item, quantity):  # add size

        """
        Adding to session data
        """

        item_id = str(item.id)

        if item_id in self.cart:
            self.cart[item_id]['quantity'] = quantity
            # self.cart[item_id]['size'] = size

        else:
            self.cart[item_id] = {
                'price': str(item.price),
                'quantity': int(quantity),
                # 'size': size
            }

        self.save()

    def __iter__(self):
        
        item_ids = self.cart.keys()
        items = Item.objects.filter(id__in=item_ids)
        cart = self.cart.copy()

        for item in items:
            cart[str(item.id)]['item'] = item

        for unit in cart.values():
            unit['price'] = Decimal(unit['price'])
            unit['item_total'] = unit['price'] * unit['quantity']
            yield unit

    def __len__(self):
        return sum(unit['quantity'] for unit in self.cart.values())  # do i need a size here?

    def unit_total(self):
        return sum(Decimal(unit['price']) * unit['quantity'] for unit in self.cart.values())
            
    def delete(self, item):  # and later add the size as well
        item_id = str(item)

        if item_id in self.cart:
            del self.cart[item_id]
        
        self.save()

    def update(self, item, quantity):  # and later add the size as well
        item_id = str(item)

        if item_id in self.cart:
            self.cart[item_id]['quantity'] = quantity
        
        self.save()
    

    def save(self):
        self.session.modified = True

