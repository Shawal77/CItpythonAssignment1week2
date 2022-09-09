'''
Create a nesting list that prints out the color
and the car brand.
'''
cars=[
    ['Ferrari','Black'],
    ['Mazda','White'],
    ['Ford','Green']
]

for nameColorPair in cars:
    print(f"\nThe car type {nameColorPair[0]} is of color {nameColorPair[1]}")
