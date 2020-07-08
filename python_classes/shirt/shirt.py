from Shirt_class import Shirt

shirt_one = Shirt('red', 'S', 'long-sleeve', 25, 'long')
print(shirt_one.price)
Shirt.change_price(shirt_one, 10)
print(shirt_one.price)
shirt_one.price = 50
print(shirt_one.price)
Shirt.double_price(shirt_one)
print(shirt_one.price)

shirt_two = Shirt('orange', 'L', 'short-sleeve', 10, 'short')
