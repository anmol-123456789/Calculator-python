# define a function
def calculator(exp):
    return eval(exp)

expression = input("Enter your mathematical Expression: ")

result = calculator(expression)  # call a function
print(f"{expression} = {result}")
