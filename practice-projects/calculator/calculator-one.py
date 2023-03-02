logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Division
def divide(n1, n2):
    return n1 / n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

"""
function = operations["+"]
function(2, 3)
"""

num1 = int(input("whats the first number?: "))
num2 = int(input("whats the second number?: "))

for symbol in operations:
    print (symbol)

operation_symbol = input("Pick an operation from the line above: ")
calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")

sec_operation_symbol = input("Pick an operation from the line above: ")
num3 = int(input("Whats the next number?:"))
calculation_function = operations[sec_operation_symbol]
sec_answer = calculation_function(answer, num3)

print(f"{answer} {sec_operation_symbol} {num3} = {sec_answer} ")

