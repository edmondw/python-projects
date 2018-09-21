arrow_base_height = int(input('Enter arrow base height: \n'))
arrow_base_width = int(input('Enter arrow base width: \n'))

# Ask user for an arrow head width until head width is larger than arrow base width.
arrow_head_width = 0
while (arrow_head_width <= arrow_base_width):
    print('Enter arrow head width: ')
    arrow_head_width = int(input())

# Draw arrow base.
for i in range(arrow_base_height):
    for j in range(arrow_base_width):
        print('*', end='')
    print('')

# Draw arrow head.
for i in range(arrow_head_width, 0, -1):
    for j in range(i):
        print('*', end='')
    print('')
