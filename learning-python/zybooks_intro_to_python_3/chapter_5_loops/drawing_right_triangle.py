'''
Drawing A Right Triangle

The following program a right triangle based on user input.
Date: 2018-20-09
Author: Edmond Weiss
'''

triangle_char = input('Enter a character: \n')
triangle_height = int(input('Enter triangle height: \n'))

for triangle_width in range(1, triangle_height + 1):
    for j in range(triangle_width):
        print(triangle_char, end=' ')
    print('')
