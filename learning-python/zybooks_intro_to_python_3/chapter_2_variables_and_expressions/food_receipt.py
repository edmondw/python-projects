# Part 1
item_name = input('Enter food item name: \n')
item_price = float(input('Enter item price: \n'))
item_quantity = int(input('Enter item quantity: \n\n'))
item_total_cost = item_quantity * item_price

print('RECEIPT')
print(item_quantity, item_name, '@ $', item_price, '= $', item_total_cost)
print('Total cost: $', item_total_cost, end='\n\n\n')

# Part 2
item2_name = input('Enter second food item name: \n')
item2_price = float(input('Enter item price: \n'))
item2_quantity = int(input('Enter item quantity: \n\n'))
item2_total_cost = item2_price * item2_quantity
print('RECEIPT')
print(item_quantity, item_name, '@ $', item_price,
      '= $', item_total_cost, end='\n')
print(
    item2_quantity,
    item2_name, '@ $',
    item2_price, '= $',
    item2_total_cost,
    end='\n'
)
order_total_cost = item_total_cost + item2_total_cost
print('Total cost: $', order_total_cost, end='\n\n')

# Part 3
GRATUITY_RATE = .15
gratuity = order_total_cost * GRATUITY_RATE
print('15% gratuity: $', gratuity)
print('Total with tip: $', order_total_cost + gratuity)
