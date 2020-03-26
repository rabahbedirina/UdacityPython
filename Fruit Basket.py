# You would like to count the number of fruits in your basket.
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits, but you do not want to count the other items in your basket.
# Iterate through the dictionary

# if the key is in the list of fruits, add the value (number of fruits) to fruit_count, not_fruit_count


def fruit_Basket(fruit_count, not_fruit_count, fruits, basket_items):

    for item, number in basket_items.items():

        if item not in fruits:
            not_fruit_count += number
        else:
            fruit_count += number
    return print("fruit", fruit_count, "Not fruit", not_fruit_count)


fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']
fruit_Basket(fruit_count, not_fruit_count, fruits, basket_items)
fruit_count, not_fruit_count = 0, 0
basket_items = {'pears': 5, 'grapes': 19,
                'kites': 3, 'sandwiches': 8, 'bananas': 4}
fruit_Basket(fruit_count, not_fruit_count, fruits, basket_items)
fruit_count, not_fruit_count = 0, 0
basket_items = {'peaches': 5, 'lettuce': 2,
                'kites': 3, 'sandwiches': 8, 'pears': 4}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']
fruit_Basket(fruit_count, not_fruit_count, fruits, basket_items)
fruit_count, not_fruit_count = 0, 0
basket_items = {'lettuce': 2, 'kites': 3,
                'sandwiches': 8, 'pears': 4, 'bears': 10}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']
fruit_Basket(fruit_count, not_fruit_count, fruits, basket_items)
