def is_Odd(number):
    if number % 2 !=0:
        return True
    
def factorial(number):
    """ Factorial function """
    if number < 0:
        return "Invalid Number"
    elif number == 0:
        return 1
    else:
        result = 1
        for num in range(1, number+1):
            result *= num
        return result

print(factorial(0))