a = int(input("Enter 1st num:"))
b = int(input("Enter 2nd num:"))

try:
    print(a/b)
except Exception:
    print("can't divide by zero")
finally:
    print("operation done")

