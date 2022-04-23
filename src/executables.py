##
# @file executables.py
#
# @brief Modul pro výpis do GUI a pro volání funkcí z matematické knihovny. 
#
# @author Miroslav Bálek (xbalek02), Kristián Dobeš (xdobes22), Maroš Synák (xsynak03), Jan Král (xkralj12)
# @version 1.0
#
# @section DESCRIPTION
#
# Modul slouží k výpisu do GUI. Po zadání inputu rozlišuje zadané operace a zajišťuje volání správných funkcí z matematické knihovny.
# 


import gui
import tkinter
from sympy import pretty_print
from sympy.abc import a, b, n
from tkinter.tix import *
import math_library

##
# @brief Funkce pro vypsání čísla 1 do GUI okna 
# 
def print_1(ignore=0):
    gui.display.configure(state='normal')
    gui.display.insert(END,"1")
    gui.display.configure(state='disabled')

##
# @brief Funkce pro vypsání čísla 2 do GUI okna 
# 
def print_2(ignore=0):
    gui.display.configure(state='normal')
    gui.display.insert(END,"2")
    gui.display.configure(state='disabled')

##
# @brief Funkce pro vypsání čísla 3 do GUI okna 
# 
def print_3(ignore=0):
    gui.display.configure(state='normal')
    gui.display.insert(END,"3")
    gui.display.configure(state='disabled')

##
# @brief Funkce pro vypsání čísla 4 do GUI okna 
# 
def print_4(ignore=0):
    gui.display.configure(state='normal')
    gui.display.insert(END,"4")
    gui.display.configure(state='disabled')

##
# @brief Funkce pro vypsání čísla 5 do GUI okna 
# 
def print_5(ignore=0):
    gui.display.configure(state='normal')
    gui.display.insert(END,"5")
    gui.display.configure(state='disabled')

##
# @brief Funkce pro vypsání čísla 6 do GUI okna 
# 
def print_6(ignore=0):

    gui.display.configure(state='normal')
    gui.display.insert(END,"6")
    gui.display.configure(state='disabled')

##
# @brief Funkce pro vypsání čísla 7 do GUI okna 
# 
def print_7(ignore=0):
    gui.display.configure(state='normal')
    gui.display.insert(END,"7")
    gui.display.configure(state='disabled')

##
# @brief Funkce pro vypsání čísla 8 do GUI okna 
# 
def print_8(ignore=0):
    gui.display.configure(state='normal')
    gui.display.insert(END,"8")
    gui.display.configure(state='disabled')

##
# @brief Funkce pro vypsání čísla 9 do GUI okna 
# 
def print_9(ignore=0):
    gui.display.configure(state='normal')
    gui.display.insert(END,"9")
    gui.display.configure(state='disabled')

##
# @brief Funkce pro vypsání čísla 0 do GUI okna 
# 
def print_0(ignore=0):
    gui.display.configure(state='normal')
    gui.display.insert(END,"0")
    gui.display.configure(state='disabled')

##
# @brief Funkce pro vypsání znaku + do GUI okna 
# 
def print_plus(ignore=0):
    gui.display.configure(state='normal')
    gui.display.insert(END,"+")
    gui.display.configure(state='disabled')

##
# @brief Funkce pro vypsání znaku - do GUI okna 
#     
def print_minus(ignore=0):
    gui.display.configure(state='normal')
    gui.display.insert(END,"-")
    gui.display.configure(state='disabled')

##
# @brief Funkce pro vypsání znaku * do GUI okna 
# 
def print_mul(ignore=0):
    gui.display.configure(state='normal')
    gui.display.insert(END,"*")
    gui.display.configure(state='disabled')

##
# @brief Funkce pro vypsání znaku / do GUI okna 
# 
def print_div(ignore=0):
    gui.display.configure(state='normal')
    gui.display.insert(END,"/")
    gui.display.configure(state='disabled')

##
# @brief Funkce pro vypsání znaku ^ do GUI okna 
# 
def print_n_pow(ignore=0):
    gui.display.configure(state='normal')
    gui.display.insert(END,"^")
    gui.display.configure(state='disabled')

##
# @brief Funkce pro vypsání znaku √ do GUI okna 
# 
def print_n_root(ignore=0):
    gui.display.configure(state='normal')
    gui.display.insert(END,"√")
    gui.display.configure(state='disabled')


#def print_lp(ignore=0):
 #   display.configure(state='normal')
#    display.insert(END,"(")
#    display.configure(state='disabled')
#def print_rp(ignore=0):
#    display.configure(state='normal')
#    display.insert(END,")")
#    display.configure(state='disabled')

##
# @brief Funkce pro vypsání znaku .\ do GUI okna 
# 
def print_dot():
    gui.display.configure(state='normal')
    gui.display.insert(END,".")
    gui.display.configure(state='disabled')
  
##
# @brief Funkce pro vypsání znaku ! do GUI okna 
# 
def print_fac(ignore=0):
    gui.display.configure(state='normal')
    gui.display.insert(END,"!")
    gui.display.configure(state='disabled')

##
# @brief Funkce pro vypsání znaku % do GUI okna 
#
def print_mod(ignore=0):
    gui.display.configure(state='normal')
    gui.display.insert(END,"%")
    gui.display.configure(state='disabled')

##
# @brief Funkce pro volání funkcí z knihovny mathlibrary.\py
#
def execute():
    gui.display.configure(state = 'normal')
    equation = gui.display.get("1.0",END)
    #print(equation)
    num = ""
    appended_sign = 0
    arr_inputs = []
    ex = 0
    minus_num=0
    for i in equation: #prochází input znak po znaku
        if i in ('1','2','3','4','5','6','7','8','9','0'): #pokud obsahuje číslici 
            if (appended_sign == 2):
                gui.display.delete("1.0",END)
                gui.display.insert("1.0","Synatax error")
                ex = 1
            appended_sign = 0
            if (minus_num == 1):
                num += '-'
                minus_num=0
            num += i
        else:
            if appended_sign == 1:
                gui.display.delete("1.0",END)
                gui.display.insert("1.0","Synatax error")
                ex = 1
            if num != "":
                arr_inputs.append(num)
            if i != '\n' and num=="" and appended_sign==0:
                minus_num=1
                continue
            elif i != '\n':
                arr_inputs.append(i)
                if (i != '!'):
                    appended_sign=1
                else:
                    appended_sign=2
            num=""

    if ex == 1:
        return
    #factorial
    to_delete = []
    length = len(arr_inputs)                              #!nevyužitá proměná? 
    for i in range(0,len(arr_inputs)):                    #prochází pole znak po znaku
        if arr_inputs[i] == '!':                          #pokud prvek pole obsahuje "operaci"
            to_delete.append(i)                           #přidá danou operaci do array pro smazání 
            number = int(arr_inputs[i-1])                 #nastaví number na hodnotu čísel před operací
            arr_inputs[i-1] = math_library.fac(number)    #zapíše na pozici čísla v poli výsledek operace
            #for o in range(i+1,len(arr_inputs)):
               # arr_inputs[o-1]=arr_inputs[o]
    for i in reversed(to_delete):                         #odstranění přebytečných znaků z pole
        arr_inputs.pop(i)
    to_delete = []
    
    #root
    for i in range(0,len(arr_inputs)):
        if arr_inputs[i] == '√':
            to_delete.append(i)
            to_delete.append(i+1)
            number1 = int(arr_inputs[i-1])
            number2 = int(arr_inputs[i+1])
            arr_inputs[i-1] = math_library.root(number2,number1)
    for i in reversed(to_delete):
        arr_inputs.pop(i)
    to_delete = []

    #pow
    for i in range(0,len(arr_inputs)):
        if arr_inputs[i] == '^':
            to_delete.append(i)
            to_delete.append(i+1)
            number1 = int(arr_inputs[i-1])
            number2 = int(arr_inputs[i+1])
            arr_inputs[i-1] = math_library.mypow(number1,number2)
    for i in reversed(to_delete):
        arr_inputs.pop(i)
    to_delete = []

    #div
    for i in range(0,len(arr_inputs)):
        if arr_inputs[i] == '/':
            to_delete.append(i)
            to_delete.append(i+1)
            number1 = int(arr_inputs[i-1])
            number2 = int(arr_inputs[i+1])
            arr_inputs[i-1] = math_library.div(number1,number2)
    for i in reversed(to_delete):
        arr_inputs.pop(i)
    to_delete = []
    
    #rem
    for i in range(0,len(arr_inputs)):
        if arr_inputs[i] == '/':
            to_delete.append(i)
            to_delete.append(i+1)
            number1 = int(arr_inputs[i-1])
            number2 = int(arr_inputs[i+1])
            arr_inputs[i-1] = math_library.rem(number1,number2)
    for i in reversed(to_delete):
        arr_inputs.pop(i)
    to_delete = []
    #mult
    for i in range(0,len(arr_inputs)):
        if arr_inputs[i] == '*':
            to_delete.append(i)
            to_delete.append(i+1)
            number1 = int(arr_inputs[i-1])
            number2 = int(arr_inputs[i+1])
            arr_inputs[i-1] = math_library.mult(number1,number2)
    for i in reversed(to_delete):
        arr_inputs.pop(i)
    to_delete = []

    #sub
    for i in range(0,len(arr_inputs)):
        if arr_inputs[i] == '-':
            to_delete.append(i)
            to_delete.append(i+1)
            number1 = int(arr_inputs[i-1])
            number2 = int(arr_inputs[i+1])
            arr_inputs[i-1] = math_library.sub(number1,number2)
    for i in reversed(to_delete):
        arr_inputs.pop(i)
    to_delete = []

    #sum
    for i in range(0,len(arr_inputs)):
        if arr_inputs[i] == '+':
            to_delete.append(i)
            to_delete.append(i+1)
            number1 = int(arr_inputs[i-1])
            number2 = int(arr_inputs[i+1])
            arr_inputs[i-1] = math_library.sum(number1,number2)
    for i in reversed(to_delete):
        arr_inputs.pop(i)
    to_delete = []

    gui.display.delete("1.0",END)
    gui.display.insert("1.0",str(arr_inputs[0]))
    gui.display.configure(state='disabled')

##
# @brief Funkce pro smazání posledního znaku GUI okna
#
def del_last_pos(ignore=0):
    gui.display.configure(state='normal')
    gui.display.delete("end-2c")
    gui.display.configure(state='disabled')

##
# @brief Funkce pro smazání obsahu GUI okna
# 
def del_all():
    gui.display.configure(state='normal')
    gui.display.delete("1.0",END)
    gui.display.configure(state='disabled')
