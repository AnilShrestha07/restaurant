from django.conf import settings
from .models import Foods

class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        
        if not cart:
           cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
        
    def __iter__(self):
        for p in self.cart.keys():
            self.cart[str(p)]['food'] = Foods.objects.get(pk=p)
        
        for item in self.cart.values():
            item['total_price'] = int(item['food'].price*item['quantity'])  
            
            yield item
            
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values()) 
    
    
    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True
        
    def add(self, food_id,quantity=1, update_quantity=False):
        food_id = str(food_id)
        
        if food_id not in self.cart:
            self.cart[food_id] = {
                'quantity': int(quantity),
                'id' : food_id
            }
        if update_quantity:
            self.cart[food_id]['quantity'] += int(quantity)
            
            if self.cart[food_id]['quantity'] <= 0:
                self.remove(food_id)
        self.save()  
        
    def remove(self,food_id):
        if food_id in self.cart:
            del self.cart[food_id]
            self.save()
    
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
        
    def get_total_cost(self):
        for p in self.cart.keys():
            self.cart[str(p)]['food'] = Foods.objects.get(pk=p)
        
        return int(sum(item['food'].price*item['quantity'] for item in self.cart.values()))

            