try:
    n1 = int(input("Enter a number: "))
    n2 = int(input("Enter another number: "))

    print('Division:', n1/n2)

except ValueError:
    print("Please enter a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
except Exception as e:
    print("An error occurred. ", e)


