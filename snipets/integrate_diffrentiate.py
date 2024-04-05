from sympy import symbols, diff, integrate, sympify
x = symbols('x')
user_input = input("Enter the function to integrate, in terms of x: ")
expr = sympify(user_input)
result = integrate(expr, x)
print(f"The integral of {user_input} is: {result}")

from sympy import symbols, diff, integrate, sympify
x = symbols('x')
user_input = input("Enter the function to differentiate, in terms of x: ")
expr = sympify(user_input)
result = diff(expr, x)
print(f"The derivative of {user_input} with respect to x is: {result}")