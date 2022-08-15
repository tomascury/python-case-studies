try:
    arg = int("sss")
except ValueError as err:
    print("Invalid input --- " + str(err))

try:
    value = 10 / 0
except ZeroDivisionError:
    print("Divided by Zero")
