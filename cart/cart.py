from product.models import Product


CART_SESSION_ID = 'cart'
class Cart:
    def __init__(self,request) -> None:
        self.session = request.session
        
        cart = self.session.get(CART_SESSION_ID)
        
        if not cart:
            cart = self.session[CART_SESSION_ID] = {}
        
        self.cart = cart
    
    def update_quantity(self,item_id,quantity):
        for key, item in self.cart.items():
            if item['id'] == item_id:  
                self.cart[key]['quantity'] = quantity
                break
        self.save()  
    
    def unique_id_generator(self,id,color):
        result = f'{id}-{color}'
        return result
    
    
    def add(self,product,quantity,color, update_quantity=False):
        
        unique = self.unique_id_generator(product.id,color)
        if unique not in self.cart:
            self.cart[unique] = {
                'quantity':0, 
                'price': str(product.price),
                'color': color
                ,'id':product.id
            }
            
            if update_quantity:
                self.cart[unique]['quantity'] = int(quantity)

            else:
                self.cart[unique]['quantity'] += int(quantity)
            
        
        self.save()
    
    def delete(self,id):
        if id in self.cart:
            del self.cart[id]
            self.save()

        if "selected_color" in self.session:
            del self.session['selected_color']
        
    def __iter__(self):
        cart = self.cart.copy()
        
        for item in cart.values():
            product = Product.objects.get(id=int(item['id']))
            item['product'] = product
            item['total'] = int(item['quantity']) * int(item['price'])
            item['unique_id'] = self.unique_id_generator(product.id,item['color'])
            
            yield item
    
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    
    def clear(self):
        del self.session[CART_SESSION_ID]
        self.save()
        
        if "selected_color" in self.session:
            del self.session['selected_color']
        
    
    def total_price(self):
        cart = self.cart.values()
        print(cart)
        total = sum([int(item['price']) * int(item['quantity']) for item in cart])
        return total
        
        
    
    def save(self):
        self.session.modified = True