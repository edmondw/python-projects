import math

wall_height_in_feet = int(input('Enter wall height (feet): \n'))
wall_width_in_feet = int(input('Enter wall width (feet): \n'))
wall_area_in_sq_feet = float(wall_height_in_feet * wall_width_in_feet)
WALL_AREA_COVERED_BY_GALLON = 350
paint_needed_in_gallons = wall_area_in_sq_feet / WALL_AREA_COVERED_BY_GALLON
one_gallon_cans_needed = math.ceil(paint_needed_in_gallons)
color_cost = {
    'red': 35,
    'green': 23,
    'blue': 25
}
print('Wall area:', wall_area_in_sq_feet, 'square feet')
print('Paint needed:', paint_needed_in_gallons, 'gallons')
print('Cans needed:', one_gallon_cans_needed, 'can(s)')
chosen_paint_color = input('Choose a color to paint the wall: \n')
cost = one_gallon_cans_needed * color_cost[chosen_paint_color]
print('Cost of purchasing red paint:$', cost)
