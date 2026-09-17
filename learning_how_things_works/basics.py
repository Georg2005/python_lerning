from functools import reduce


print(type(5))  # <class 'int'>
print(type(3.14))  # <class 'float'>
print(type("Hello"))  # <class 'str'>
print(type(True))  # <class 'bool'>
print(type(None))  # <class 'NoneType'>

#Operations on data
    #Integer operations
x = 10
y = 3 
z = x + y  # Addition
z1 = x - y  # Subtraction
z2 = x * y  # Multiplication
z3 = x / y  # Division
print((z*4+2-3)/z3)  # Output: 52

    #Float operations
a = 5.5
b = 2.0
c = a + b  # Same operations as integers
a = b 
print(a, b)  # Output: 2.0, 5.5

    #String operations
s1 = "Hello"
s1 += " World"  # Concatenation
s2 = s1 * 3  # Repetition
print(s1)  # Output: Hello World
s3 = 'PYTHON'
print(s2 + "!")  # Output: Hello WorldHello WorldHello World!
print(s3.lower())  # Converts to lowercase Output: python
#Upper() is used to convert a string to uppercase

print(len(s1)) # Counting how many characters are in the string Output: 11


name = "George" 
age = 20
print(f"My name is {name} and I am {age} years old.") 

    #Boolean operations
p = True
q = False
r = p and q  # Logical AND
s = p or q  # Logical OR
t = not p  # Logical NOT
print(r, s, t)  # Output: False True False

    #NoneType operations
n = None
print(n is None)  # Output: True
print(n is not None)  # Output: False

#OPERATORS
    #Arithmetic operators
    # +, -, *, /, %, **
    #Comparison operators
    # ==, !=, >, <, >=, <=
    #Logical operators
    # and, or, not
    #Assignment operators
    # =, +=, -=, *=, /=, %=, **=
    #Bitwise operators
    # &, |, ^, ~, <<, >>
    #Membership operators
    # in, not in
    #Identity operators
    # is, is not
    #Conditional operators
    # if, elif, else

x = input("Enter a number: ")
if x.isdigit():
    x = int(x)
    if x > 0:
        print("The number is positive.")
    elif x < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")

x1 = input("Enter a number: ")        
if x1.isdigit():
    x1 = int(x1)
else:
    x1 = print("Invalid input. Please enter a valid number.")
    if x1 > 3:
        print("The number is greater than 3")
    elif x1 < 3:
        print("The number is less than 3")
    else:
        print("The number is equal to 3")

#LISTS
my_list = [1, 2, 3, 4, 5, 'Hello', 3.14, True, None, [6, 7, 8]] # Better not to use
print(my_list)  # Output: [1, 2, 3, 4, 5, 'Hello', 3.14, True, None, [6, 7, 8]]

my_list1 = [1, 2, 3, 4, 5]  # A list of integers
my_list2 = [7,8,9]
my_list3 = my_list1 + my_list2  # Concatenation of two lists

element1 = 'Banana'
element2 = 'Apple'
element3 = 'Orange'
my_list4 = [element1, element2, element3]  # A list of variables

print(my_list1)  # Output: [1, 2, 3, 4, 5, 6]
print(my_list3)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list4)  # Output: ['Banana', 'Apple', 'Orange']

word = "Hello"
my_list5 = list(word)  # Convert a string to a list of characters
print(my_list5)  # Output: ['H', 'e', 'l', 'l', 'o']

fruits = ['Apple', 'Banana', 'Orange', 'Grapes']
fruits.append(['Mango', 'Watermelon'])  # Add an element to the end of the list

fruits.insert(1, 'Pineapple')  # Insert an element at a specific index

fruits.remove('Banana')  # Remove an element from the list


print(fruits)  # Output: ['Apple', 'Pineapple', 'Orange', 'Grapes', ['Mango', 'Watermelon']]

last_fruits = fruits.pop()  # Remove and return the last element of the list
print(last_fruits)  # Output: ['Mango', 'Watermelon']

fruits1 = ['Apple', 'Banana', 'Orange', 'Grapes']
fruits1.sort()  # Sort the list in ascending order

print(fruits1)  # Output: ['Apple', 'Banana', 'Grapes', 'Orange']

fruits2 = ['Apple', 'Banana', 'Orange', 'Grapes']
fruits2.sort(reverse=True)  # Sort the list in descending order
print(fruits2)  # Output: ['Orange', 'Grapes', 'Banana', 'Apple']

my_list4.reverse()  # Reverse the order of the list
print(my_list4)  # Output: ['Orange', 'Apple', 'Banana']

my_string = "My name is George, and I love programming."
my_list6 = my_string.split(" ")  # Split the string into a list of substrings
print(my_list6)  # Output: ['My', 'name', 'is', 'George,', 'and', 'I', 'love', 'programming.']

joined_string = " ".join(my_list6)  # Join the list of substrings into a single string
print(joined_string)  # Output: My name is George, and I love programming.

my_list7 = [14, 4, 7, 2, 9, 1, 5]
min_value = min(my_list7)  # Find the minimum value in the list
sum_value = sum(my_list7)  # Find the sum of all values in the list
print(min_value)  # Output: 1
print(max(my_list7))  # Output: 14
print(sum_value)  # Output: 42
print(type(my_list7))  # Output: <class 'list'>
print(len(my_list7))  # Output: 7

#INDEXING AND SLICING
    #An index gets a single item from a list, while a slice gets a range of items.
    # The conveyor belt of ducks
ducks = ['yellow', 'yellow', 'red', 'yellow', 'blue', 'yellow']

# Checking the 3rd duck (remember, counting starts at 0!)
third_duck = ducks[2]
print(third_duck)  # Output: red

# Checking a slice of ducks (from index 1 to 4)
slice_of_ducks = ducks[1:4]
print(slice_of_ducks)  # Output: ['yellow', 'red', 'yellow']

# Grabbing ducks from index 1 up to (but not including) index 5
duck_sample = ducks[1:5]
print(duck_sample)  # Output: ['yellow', 'red', 'yellow', 'blue']

# Take every 2nd duck from the whole line using a "step" of 2
every_other_duck = ducks[::2]
print(every_other_duck)  # Output: ['yellow', 'red', 'blue']

# Use a negative index to grab the very last duck
last_duck = ducks[-1]
print(last_duck)  # Output: yellow

#LOOPS
file_list = ['Tests.txt', 'Document.txt', 'Python.txt', 'Programming.txt']
for file in file_list:
    print(file)  # Output: Tests.txt Document.txt Python.txt Programming.txt
    for char in file:
        print(char)  # Nested loop Output: Each character in the file name on a new line

numbers = [1, 2, 3, 4, 5]
for number in numbers:
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")  # Output: 1 is odd. 2 is even. 3 is odd. 4 is even. 5 is odd.


for i in range(5):  # Loop from 0 to 4
    print(i-1)  # Output: -1 0 1 2 3


for i in range(1, 10, 2):  # Loop from 1 to 9 with a step of 2
    print(i)  # Output: 1 3 5 7 9

numbers1 = [1, 2, 3, 4, 5]
for i in range(len(numbers1)):
    numbers1[i] *= 2  # Double each number in the list
print(numbers1)  # Output: [2, 4, 6, 8, 10]

greetings = "Hello World, we are learning Python!"

indexes = []
count = 0

for i in range(len(greetings)):
    if greetings[i] == 'o':
        indexes.append(i)
        count += 1

print(f"The letter 'o' appears {count} times at the following indexes: {indexes}")  # Output: The letter 'o' appears 3 times at the following indexes: [4, 7, 24]

#Multiplication table using nested loops

numbers2 = list(range(1, 10))

for i in range(len(numbers2)):
    for j in range(i, len(numbers2)):
        value_table = numbers2[i] * numbers2[j]
        print(f"{numbers2[i]} x {numbers2[j]} = {value_table}")  # Output: Multiplication table for numbers 1 to 9

print('\n\n\n')
#Multiplication table using matrix style nested loops
numbers3 = list(range(1, 10))

for col in range(len(numbers3)):
    for row in range(len(numbers3)):
        value_table = numbers3[col] * numbers3[row]
        print(f"{numbers3[col]} x {numbers3[row]} = {value_table}")  # Output: Multiplication table for numbers 1 to 9

numbers4 = list(range(1, 10))

#FUNCTIONS
def finding_average(numbers):
    for number in numbers:
        total += number
    average = total / len(numbers)
    return average

print(finding_average(numbers4))  # Output: 5.5


def finding_vowels(string):
    VOWELS = "aeiouAEIOU"
    count = 0 
    for char in string:
        if char in VOWELS:
            count += 1
    return count

def finding_consonants(string):
    VOWELS = "aeiouAEIOU"
    count = 0 
    for char in string:
        if char.isalpha() and char not in VOWELS: # .isalpha() checks if the character is an alphabet letter
            count += 1
    return count

print(finding_vowels("Hello World, we are learning Python!"))  # Output: 10
print(finding_consonants("Hello World, we are learning Python!"))  # Output: 13


def nothing():
    pass  # This function does nothing.

nothing()  # Output: This function does nothing.

#Complicated function with multiple parameters and type hints
def greeting(*, name: str, age: int):
    print(f"Hello! My name is {name} and I am {age} years old.")

# Validate name input
while True:
    input_name = input("Enter your name: ")
    if input_name.isalpha():
        break
    print("Invalid input. Please enter a valid name.")

# Validate age input
while True:
    input_age = input("Enter your age: ")
    if input_age.isdigit():
        input_age = int(input_age)
        break
    print("Invalid input. Please enter a valid age.")

greeting(name=input_name, age=input_age)


#  VARIABLE SCOPE

x = 10  # Global variable
def print_values():
    x=5  # Local variable
    print(f"Local x: {x}")  # Output: Local x: 5
print_values()  #BETTER NOT TO USE SAME GLOBAL WITH LOCAL VARIABLES

#  BETTER USE CONSTANTS FOR GLOBAL VARIABLES
PI = 3.14159  # Constant variable

def calculate_area(radius):
    area = PI * radius ** 2  # Use the constant variable
    return area

calculate_area(5)  # Output: 78.53975

#  Good practice to use constants for global variables that should not change.
DEFAULT_LEVEL_EXPERIENCE = 200

def calculate_experience(*, gained_experience: int, current_experience: int):
    total_experience = gained_experience + current_experience 
    level_up = False

    if total_experience >= DEFAULT_LEVEL_EXPERIENCE:
        level_up = True

    return total_experience

calculate_experience(gained_experience=150, current_experience=100)  # Output: 250
calculate_experience(gained_experience=50, current_experience=100)  # Output: 150


#  WHILE LOOP

counter = 0
while counter <=5:
    print(f"Counter: {counter}")  # Output: Counter: 0, Counter: 1, Counter: 2, Counter: 3, Counter: 4, Counter: 5
    counter += 1


my_list8 = [1, 2, 3, 4, 5]

while my_list8:
    print(f"Element: {my_list8.pop()}")  # Output: 5, 4, 3, 2, 1


while True:
    answer = input("Do you want to continue? (yes/no): ")
    if answer.lower() == "no":
        print("Exiting the loop.")
        break
    elif answer.lower() == "yes":
        print("Continuing the loop.")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")


#  TUPLES

my_tuple = (1, 2, 3, 4, 5)
my_tuple1 = ('apple', 'banana', 'cherry')

type(my_tuple)  # Output: <class 'tuple'>
type(my_tuple1[0])  # Output: <class 'str'>

var1, var2, var3 = my_tuple  # Unpacking a tuple
print(var1, var2, var3)  # Output: 1 2 3

#  DICTIONARIES
person = {
    "name": "George",
    "age": 20,
    "city": "New York"
}

print(person["name"])  # Output: George

person["age"] = 21  # Update value
person["country"] = "USA"  # Add new key-value pair

print(person)  # Output: {'name': 'George', 'age': 21, 'city': 'New York', 'country': 'USA'}

person.pop("city")  # Remove key-value pair
print(person)  # Output: {'name': 'George', 'age': 21, 'country': 'USA'}

additional_info = {
    "city": "Ukraine",
    "married": "False",
    "occupation": "student/Engineer"
}

person.update(additional_info)
# person = person | additional_info - another way to update info in dictioonary
print(person)

#  ADVANCED FUNCTIONS

def add_all(*args):
    summary = 0
    for num in args:
        summary += num
    return summary

print(add_all(1,2,3,4,5)) 

values2 = [1,2,3,4,5]
values3 = [1,2,3,4,5]
print(add_all(*values2, *values3)) # Using int 

def introduce(**kwargs):
    print(kwargs)
    print(type(kwargs))

introduce(name='Joe', age = 20, city = "New York") # Using str 

person = {
    "name": "George",
    "age": 20,
    "city": "Kyiv"
}

introduce(**person) # Using dictionary to show how advanced funcs works

def introduce_all_args(x:int, y:int, *args, value: int = 6, **kwargs):
    print(x,y) 
    print(args)
    print(value)
    print(kwargs)


introduce_all_args(1, 2, 3, 4, 5, **person)

def modify_dict(old_dict: dict, **kwargs) -> tuple[dict, bool]:
    is_modified = False

    for key, value in kwargs.items():
        if old_dict.get(key) != value:
            old_dict[key] = value
            is_modified = True

    return old_dict, is_modified


product = {'id': 1, 'name': 'Laptop', 'price': 999.99}

structure = modify_dict(old_dict=product, in_stock=True)
print(type(structure))
print(structure)

product, was_modified = modify_dict(old_dict=product, in_stock=True)
print(product)  # Outputs: {'id': 1, 'name': 'Laptop', 'price': 999.99, 'in_stock': True}
print(was_modified)  # Outputs: True

product, was_modified = modify_dict(old_dict=product, id=1, name="Laptop")
print(product)  # Outputs: {'id': 1, 'name': 'Laptop', 'price': 999.99, 'in_stock': True}
print(was_modified)  # Outputs: False

#  RECURSION
def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

factorial(5)  # Output: 120

#  LAMBDA FUNCTIONS
add = lambda x, y: x + y
print(add(5, 3))  # Output: 8

# MAP, FILTER, REDUCE

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
reduced_product = reduce(lambda x, y: x * y, numbers)
print(reduced_product)  # Output: 120
numbers1 = [2,5,8,1,4,7,3,6]
filtered_numbers = list(filter(lambda x: x > 4, numbers1))
print(filtered_numbers)  # Output: [5, 8, 7, 6]

#  LIST COMPREHENSIONS
numbers2 = [1, 2, 3, 4, 5]
squared_numbers1 = [x**2 for x in numbers2]
print(squared_numbers1)  # Output: [1, 4, 9, 16, 25]


# 4 built-in data types in Python used to store collections of data: List, Tuple, Set, and Dictionary. Each has its own characteristics and use cases.

my_list9 = [1, 2, 3, 4, 5]  # List: Ordered, mutable, allows duplicates
my_tuple9 = (1, 2, 3, 4, 5)  # Tuple: Ordered, immutable, allows duplicates
my_set9 = {1, 2, 3, 4, 5}  # Set: Unordered, mutable, no duplicates
my_dict9 = {"a": 1, "b": 2, "c": 3}  # Dictionary: Ordered (Python 3.7+), mutable, no duplicate keys
