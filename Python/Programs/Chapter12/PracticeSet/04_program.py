try:
    a=int(input("Enter a number : "))
    b=int(input("Enter a number : "))
    print(a/b)
except ZeroDivisionError as e:
    print("Please enter a valid no.")