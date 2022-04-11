#math-library

def sum(num1, num2):
    return num1+num2

def sub(num1, num2):
    return num1-num2

def mult(num1, num2):
    return num1*num2

def div(divident, divisor):
    if divisor==0:
        print("Invalid: dividing by zero")
        quit()
        
    return divident/divisor
    
def Pow(basis, exponent):       #CAPITAL Pow
    result = pow(basis, exponent)
    return result

def nroot(num, root):
    if root==0: 
        print("Invalid: dividing by zero")
    else:
        result = num**(1/root)
        return result

def remainder(divident, divisor):
    if divisor==0:        
        print("Invalid: dividing by zero")        
    else:
        return divident%divisor

def fac(num): 
    factorial = 1
    if num<0 or num%1 != 0:
        print("Invalid: invalid factorial argument")
        return 
    elif num==0:
        result=1
    else:
        for i in range(1,num + 1):         
            factorial = factorial*i
            result = factorial

    return result
