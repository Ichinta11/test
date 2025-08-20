# Lists
nums = [10, 20, 30, 40]
print("List:", nums)
print("First element:", nums[0])  # like SQL row access
nums.append(50)  # add new element
print("After append:", nums)

# Dictionaries
student = {"name": "Indu", "age": 26, "city": "Charlotte"}
print("Dictionary:", student)
print("Student name:", student["name"])

# Loops
for n in nums:
    print("Loop element:", n)

# Functions
def square(x):
    return x ** 2

# Function definition
def only_even(numbers):
    evens = []
    for value in numbers:
        if value % 2 == 0:
            evens.append(value)
    return evens

# Example usage
my_list = [10, 21, 32, 43, 54]
print("Original list:", my_list)
print("Even numbers:", only_even(my_list))
cd path/to/python-data
git init
