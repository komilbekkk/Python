# Homework: List and Tuple Exercises

# 1

fruits = ["apple", "banana", "cherry", "orange", "grape"]
print(fruits[2]) 

# 2

l1 = [1,2,3,4,5]
l2 = [6,7,8,9,10]
l3 = l1 +l2

print("Combined list:", l3)

# 3

l4 = [1,2,3,4,5,6,7,8]

first_n = l4[0]

middle_n = l4[len(l4)//2]

last_n = l4[-1]

new_list = [first_n, middle_n, last_n]

print(new_list)

# 4

movie = ['The Godfather', 'Stive Jobs', 'Inside', 'Work', 'Jobless']

converted = tuple(movie)

print(converted)

# 5


list_of_cities = ['New York', 'London', 'Pekin', 'Tokyo', 'Tashkent', 'Berlin', 'Paris']

if 'Paris' in list_of_cities:
    print('Paris is in the list')
else:
    print('This city is not in the list')
  
# Test option

city = input('Enter your favorite city')

list_of_cities = ['New York', 'London', 'Pekin', 'Tokyo', 'Tashkent', 'Berlin', 'Paris']

if city in list_of_cities:
    print(city)
else:
    print('This city is not in the list')

# 6

number = [1,2,3,4,5,6]

dublicated = number + number

dublicated_2 = number*2

print(dublicated)
print(dublicated_2)

# 7

numbers = [1, 2, 3, 4, 5]

# Swapping first and last elements
numbers[0], numbers[-1] = numbers[-1], numbers[0]

print(numbers)


numbers = [1, 2, 3, 4, 5]

print(numbers[-1])

# 8

tuple = (1,2,3,4,5,6,7,8,9,10)

tuple[3:7]

# 9

color_list = ['blue', 'red', 'yellow', 'green', 'blue', 'black', 'pink', 'blue']

color_list.count('blue')

# 10

my_tuple_a = ('egle', 'tiger', 'bear', 'monkey', 'bull', 'lion')

my_tuple_a.index('lion')


