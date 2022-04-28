#############################################################################################################
# Název projektu: Matematická kalkulačka
# Soubor: mathlibrary.py
# Datum: 21.4.2022
# Poslední změna: 22.4.2022
# Autoři: Miroslav Bálek (xbalek02), Kristián Dobeš (xdobes22), Maroš Synák (xsynak03), Jan Král (xkralj12)
#
# Popis: Knihovna, která vykonává základní matematické operace jako sčítání, odčítání, násobení, dělení,
# celočíselný zbytek po dělení, umocnění, obecnou odmocninu a faktoriál 
#############################################################################################################

##
# @file mathlibrary.py
#
# @brief Matematická knihovna
#
# @author Miroslav Bálek (xbalek02), Kristián Dobeš (xdobes22), Maroš Synák (xsynak03), Jan Král (xkralj12)
# @version 1.0
#
# @section DESCRIPTION
#
# Knihovna, která vykonává základní matematické operace jako sčítání, odčítání, násobení, dělení,
# zbytek po dělení, umocnění, obecná odmocnina a faktoriál.
# Všechny funkce jsou testovány s přesností na sedm desetinných míst.



##
# Funkce pro sečtení dvou čísel 
# @param num1 první číslo
# @param num1 druhé číslo 
#
# @return Součet parametrů
def sum(num1, num2):  # Summation
    return num1+num2

##
# Funkce pro výpočet rozdílu dvou čísel 
# @param num1 první číslo
# @param num1 druhé číslo 
#
# @return Rozdíl parametrů
def sub(num1, num2):  # Subtraction
    return num1-num2

##
# Funkce pro výpočet součinu dvou čísel 
# @param num1 první číslo
# @param num1 druhé číslo 
#
# @return Součin parametrů
def mult(num1, num2):  # Multiplication
    return num1*num2
##
# Funkce pro výpočet součinu dvou čísel 
# @param divident dělenec
# @param divisor dělitel
#
# @return Podíl dělenec/dělitel
def div(divident, divisor):  # Division
    if divisor == 0:
        raise ZeroDivisionError("Invalid: Divisor cannot be 0")
    else:
        return divident/divisor
    
##
# Funkce pro výpočet mocniny
# @param basis základ
# @param exponent exponent
#
# @return Základ na exponent    
def mypow(basis, exponent):            #Exponentiation
    result = pow(basis, exponent)
    return result

##
# Funkce pro výpočet odmocniny
# @param num odmocněnec
# @param exponent odmocnitel
#
# @return N-tá odmocnina  
def root(num, root):                #Nth-Root
    if root==0: 
        raise ZeroDivisionError("Invalid: Divisor cannot be 0")    
    else:
        result = num**(1/root)
        return result

##
# Funkce pro výpočet faktorialu
# @param input základ ve floatu
# @param num základ ve intu
# Argument funkce musí být kladné číslo menší než 170
# @return Faktoriál základu  
def fac(input):  # Factorial
    num=int(input)
    factorial = 1
    if num < 0 or num % 1 != 0:
        raise ValueError("Value needs to be a non-negative integer") # Argument funkce musí být kladné číslo
    elif num == 0:
        result = 1
    elif num > 170:
        raise OverflowError("Factorial above 170") # Argument funkce musí být číslo menší než 170
    else:
        for i in range(1, num + 1):
            factorial = factorial*i
            result = factorial

    # return ("{:e}".format(result))        #returns factorial as Scientific Notation
    return result  # returns factorial as Integer

##
# Funkce pro výpočet zbytku po dělení 
# @param divident dělenec
# @param divisor dělitel
#
# @return Zbytek dělenec%\ dělitel
def rem(divident, divisor):  # Division Remainder
    if divisor == 0 or divisor == {}:
        raise ZeroDivisionError("Invalid: Divisor cannot be 0")
    else:
        return divident % divisor
    
