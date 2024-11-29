def calculator():

    Math_Operator = input("Enter your first operator (+-*/): ")
    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))

    if Math_Operator == "+":
        return num1 + num2
        print(round(result, 4))

    elif Math_Operator == "-":
        return num1 - num2
        print(round(result, 4))

    elif Math_Operator == "*":
        return num1 * num2
        print(round(result, 4))

    elif Math_Operator == "/":
        return num1 / num2
        print(round(result, 4))

    else:
        return "Math_Operator is not a preferred operator!"
    

result = calculator()
print(result)

