
# A simple calculator build on python ------->

print("A simple calculator build on Python")

fristNumber = int(input("Enter your frist number: "))
value = input("assign value (+, -, *, /, %): ")
secondNumber = int(input("Enter your second number: "))


if(value == "+"):
    print("sum result (+):", fristNumber + secondNumber)
elif(value == "-"):
    print("Subtraction result (-):", fristNumber - secondNumber)
elif(value == "*"):
    print("multiplica result (*):", fristNumber * secondNumber)
elif(value == "/"):
    print("division result (/):", fristNumber / secondNumber)
elif(value == "%"):
    print("modulus result (%):", fristNumber % secondNumber)
else:
    print("Number is not found")