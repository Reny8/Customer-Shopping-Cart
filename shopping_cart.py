class Shopping_Cart:
    def __init__(self):
        self.products = []

    def total_of_products(self):
        items_total = len(self.products)
        print(items_total)

    def add_product(self,product):
        self.products.append(product)
      
    def empty_cart(self):
        self.products = []
        return self.products
    
