def my_factorial(number):
    if number <= 1:
        return 1
    return number * my_factorial(number - 1)


def my_sum_factorial(number):
    if number <= 1:
        return 1
    return number + my_sum_factorial(number - 1)

def recursive_deposit(number):
    if number <= 1:
        return 1
    return number + my_sum_factorial(number - 1)

number = int(input("Enter the Number : "))
print(my_sum_factorial(number))
