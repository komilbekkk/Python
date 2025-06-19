# Homework Exercises

#1

name = input("Enter you name")
year = int(input("Enter your year of birth"))

age = (2025 - year)

print(f'{name}, You are {age} years old.')

#2

txt = 'LMaasleitbtui'

print(txt[0::2])
print(txt[1::2])

#3

txt = 'MsaatmiazD'

print(txt[0::2])
print(txt[::-2])

#4

txt = "I'am John. I am from London"

residence_area = txt.find("from")

print(txt[residence_area + 5:])

#5

txt = "I'am John. I am from London"
print(txt[::-1])

#6

txt = input("Enter a string")
vowels = "aeiouAEIOU"
count = 0

for char in txt:
    if char in vowels:
        count += 1

print("Number of vowels:", count)

#additional. It counts everything

txt = input("Enter a string")
count = 0
for item in txt:
    count = count + 1

print(count)

#7

l1 = list(map(int, input("Enter numbers separated by space: ").split()))
print(max(l1))

#8

word = input("Enter a word: ")

# Reverse the word using slicing
reversed_word = word[::-1]

# Compare original and reversed
if word == reversed_word:
    print("Yes, it's a palindrome!")
else:
    print("No, it's not a palindrome.")


#9

email = input("Enter your email")

domain = email[email.find('@')::]
print(domain)

#10

import random
import string

# Define the length of the password
length = int(input("Enter the desired password length: "))

# Define characters to choose from
letters = string.ascii_letters      # a-z + A-Z
digits = string.digits              # 0-9
specials = string.punctuation       # !@#$%^&*() etc.

# Combine all character types
all_chars = letters + digits + specials

# Generate random password
password = ''.join(random.choice(all_chars) for _ in range(length))

print("Generated password:", password)
