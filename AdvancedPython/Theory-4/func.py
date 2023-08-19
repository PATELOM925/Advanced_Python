from functools import reduce

def cube(y):
    return y**3

lambda_cube = lambda y: y**3

numbers = [1, 2, 3, 4, 5]

# Using a defined function
cubes = []
for y in numbers:
    cubes.append(cube(y))

print("Cubes using defined function:", cubes)

# Using a lambda function
cubes = list(map(lambda_cube, numbers))

print("Cubes using lambda function:", cubes)

# Using the filter() function
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Even numbers:", even_numbers)

# Using the reduce() function
from functools import reduce

sum_of_numbers = reduce(lambda x, y: x + y, numbers)

print("Sum of numbers:", sum_of_numbers)


