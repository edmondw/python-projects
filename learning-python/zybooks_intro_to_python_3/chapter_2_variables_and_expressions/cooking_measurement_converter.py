lemon_juice_in_cups = float(input('Enter amount of lemon juice (in cups): \n'))
water_in_cups = float(input('Enter amount of water (in cups): \n'))
agave_nectar_in_cups = float(input('Enter amount of agave (in cups): \n'))
num_of_servings = float(input('How many servings does this make? \n'))

print('Lemonade ingredients - yields', num_of_servings, 'servings')
print(lemon_juice_in_cups, 'cup(s) lemon juice')
print(water_in_cups, 'cup(s) water')
print(agave_nectar_in_cups, 'cup(s) agave nectar')

desired_servings = float(input('How many servings would you like to make? \n'))

serving_size_ratio = desired_servings / num_of_servings

print('Lemonade ingredients - yields', desired_servings, 'servings')
print(lemon_juice_in_cups * serving_size_ratio, 'cup(s) lemon juice')
print(water_in_cups * serving_size_ratio, 'cup(s) water')
print(agave_nectar_in_cups * serving_size_ratio, 'cup(s) agave nectar')

cups_in_gallon = 16

print('Lemonade ingredients - yields', desired_servings, 'servings')
print(lemon_juice_in_cups / cups_in_gallon, 'gallon(s) lemon juice')
print(water_in_cups / cups_in_gallon, 'gallon(s) water')
print(agave_nectar_in_cups / cups_in_gallon, 'gallon(s) agave nectar')
