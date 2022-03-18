from customer import Customer
from product import Product
from shopping_cart import Shopping_Cart
customer_one = Customer("Becky")
print(customer_one.customer_name)
item_1 = Product("Cheese",3.50,"Dairy")
item_2 = Product("Chicken Wings", 10.75, "Poultry")
item_3 = Product("Phone Charger", 5.99, "Electronics")
customer_one.add_new_item_to_cart(item_1)
customer_one.add_new_item_to_cart(item_2)
customer_one.add_new_item_to_cart(item_3)
shop = Shopping_Cart()
customer_one.shopping.total_of_items()
customer_one.view_cart()