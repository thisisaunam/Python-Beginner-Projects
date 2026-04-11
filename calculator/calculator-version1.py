## calculator v1: basic operations using conditionals


# taking input from user

# input 1: enter first number
num1 = float(input("enter first number: "))

# input 2: choose an operation (+, -, *, /)
operator = input("enter operator (+, -, *, /): ")

# input 3: enter second number you want to perform input 1's operation with
num2 = float(input("enter second number: ")) 

# conditional statements: perform calculation based on operator
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 == 0:
        # prevent division by zero
        result = "error: division by zero"
    else:
        result = num1 / num2
# handle invalid operator input
else:
    result = "invalid operator"

# printing final answer
print(f"{num1} {operator} {num2} = {result}")
