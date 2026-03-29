# buggy.py
print("Starting script...")

# Bug 1: division by zero
x = 10
y = 0
try:
    z = x / y
except ZeroDivisionError as e:
    print(str(e).capitalize())

# Bug 2: wrong type addition
name = "Alice"
age = "17"
greeting = name + age

# Bug 3: typo in variable


