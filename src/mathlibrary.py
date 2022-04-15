#math-library


DividingByZero=0            
InvalidFactorial=0


def sum(num1, num2):
    return num1+num2

def sub(num1, num2):
    return num1-num2

def mult(num1, num2):
    return num1*num2

def div(divident, divisor):
    if divisor==0:
        print("Invalid: dividing by zero")
        global DividingByZero             #not ideal
        DividingByZero=1
    else:
        result=divident/divisor
        return round(result,7)
    
def Pow(basis, exponent):       #CAPITAL Pow
    result = pow(basis, exponent)
    return round(result,7)

def nroot(num, root):
    if root==0: 
        print("Invalid: dividing by zero")
        global DividingByZero             #not ideal
        DividingByZero=1
    else:
        result = num**(1/root)
        return result

def rem(divident, divisor):
    if divisor==0:        
        print("Invalid: dividing by zero")
        global DividingByZero             #not ideal
        DividingByZero=1        
    else:
        return divident%divisor

def fac(num): 
    factorial = 1
    if num<0 or num%1 != 0:
        print("Invalid: invalid factorial argument")
        global InvalidFactorial
        InvalidFactorial=1
        return 
    elif num==0:
        result=1
    # elif num>170:
        
    else:
        for i in range(1,num + 1):         
            factorial = factorial*i
            result = factorial

    return result



#result=div(4,0)
result=fac(20)

print("The result is:",result)
print("Dividing by zero value:",DividingByZero)
print("Invalid Factorial Value:",InvalidFactorial)

