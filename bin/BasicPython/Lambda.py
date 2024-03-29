square = lambda a: a * a

square = lambda a: a * a

def multiple(n):
    return lambda a: n * a


mydoubler = multiple(2)
mytripler = multiple(3)

number = int(input("Enter the Number : "))
# Square a Number
print("square = ", square(number))
print("doublevalue = ", mydoubler(number))
print("tripplevalue = ", mytripler(number))
