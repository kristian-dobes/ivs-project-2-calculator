#math-library


def sum(num1, num2):                #Summation
    return num1+num2


def sub(num1, num2):                #Subtraction
    return num1-num2


def mult(num1, num2):               #Multiplication
    return num1*num2


def div(divident, divisor):         #Division
    if divisor==0:
        raise ZeroDivisionError("Invalid: Divisor cannot be 0")    
    else:
        return divident/divisor
    
    
def mypow(basis, exponent):            #Exponentiation
    result = pow(basis, exponent)
    return result


def root(num, root):                #Nth-Root
    if root==0: 
        raise ZeroDivisionError("Invalid: Divisor cannot be 0")    
    else:
        result = num**(1/root)
        return result


def fac(num):                        #Factorial
    factorial = 1
    if num<0 or num%1 != 0:
        raise ValueError("Value needs to be a non-negative integer")
    elif num==0:
        result=1
    elif num>170:
        raise OverflowError("Factorial above 170")
    else:
        for i in range(1,num + 1):         
            factorial = factorial*i
            result = factorial

    # return ("{:e}".format(result))        #returns factorial as Scientific Notation
    return result                           #returns factorial as Integer


def rem(divident, divisor):          #Division Remainder
    if divisor==0 or divisor=={}:        
        raise ZeroDivisionError("Invalid: Divisor cannot be 0")        
    else:
        return divident%divisor
