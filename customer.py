from shopping_cart import Shopping_Cart
from product import Product
class Customer:
    def __init__(self,name):
        self.customer_name = name
        self.shopping = Shopping_Cart()
    def add_new_item_to_cart(self, new_product):
        self.shopping.add_product(new_product)
    def view_cart(self):
        for item in self.shopping.products:
            print(item.product_name)
