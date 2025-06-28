# Python Dictionary and Set Exercises

# 1   

# Values

sorted_by_values_asc = dict(sorted(dict1.items(), key=lambda item: item[1]))

print(sorted_by_values_asc)

sorted_by_values_desc = dict(sorted(dict1.items(), key=lambda item: item[1], reverse=True))

print(sorted_by_values_desc)


# Keys

sorted_by_keys_desc = dict(sorted(dict1.items(), reverse = True))

print(sorted_by_keys_desc)


sorted_by_keys_asc = dict(sorted(dict1.items()))

print(sorted_by_keys_asc)

# 2

d1 = {0: 10, 1: 20}

d1.update([(2, 30)])
print(d1

# 3

union = dic1 | dic2 | dic3

print(union)

      # or
dic_all = dic1.copy()

dic_all.update(dic2)
print(dic_all)

dic_all = {**dic1, **dic2}
print(dic_all)

# 4

n = int(input("Enter a number: "))

square_dict = {}

for x in range(1, n + 1):
    square_dict[x] = x * x

print(square_dict)

# 5

squared_dict = {}

for x in range(1, 16):
    squared_dict[x] = x*x
print(squared_dict)

# Set Exercises

# 1

s1 = {1,2,3,4,2,3,4,5,6,7}
type(s1)

# 2

s2 = {'apple', 'banana', 'mango', 'nut'}

for item in s2:
    print(item)

# 3

s1 = {1,2,3,4,2,3,4,5,6,7}

s1.add(16)  #Adding one single element

s1.update([1,0,8,13,15,20,13]) #Adding multiple elements

print(s1)

# 4

s1.remove(20)

# 5

s1.discard(20)
