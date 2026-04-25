number1 = input("Enter the first number: ")
number2 = input("Enter the second number: ") 
result = int(number1) * int(number2)
if result < 0:
    print("negative")
elif result > 0:
    print("positive")
else :
    print("zero")