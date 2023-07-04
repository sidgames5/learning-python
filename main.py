# https://www.youtube.com/watch?v=rfscVS0vtbw
# left off at 2:07:18

num1 = float(input("First number: "))
num2 = float(input("Second number: "))
op = input("Operator: ")

if (op == "+"):
    print(num1 + num2)
elif (op == "-"):
    print(num1 - num2)
elif (op == "*"):
    print(num1 * num2)
elif (op == "/"):
    print(num1 / num2)
else:
    print("Error: invalid operator")
