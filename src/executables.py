#############################################################################################################
# Název projektu: Matematická kalkulačka
# Soubor: mathlibrary.py
# Datum: 22.4.2022
# Poslední změna: 24.4.2022
# Autoři: Miroslav Bálek (xbalek02), Kristián Dobeš (xdobes22), Maroš Synák (xsynak03), Jan Král (xkralj12)
#
# Modul for integrating math library with gui, takes inputs from gui uses math library to calculate results
# and delivers them back to gui
#############################################################################################################

##
# @file executables.py
#
# @brief Matematická knihovna
#
# @author Miroslav Bálek (xbalek02), Kristián Dobeš (xdobes22), Maroš Synák (xsynak03), Jan Král (xkralj12)
# @version 1.0
#
# @section DESCRIPTION
#
# Modul for integrating math library with gui, takes inputs from gui uses math library to calculate results
# and delivers them back to gui


import gui
import tkinter
from tkinter.tix import *
import mathlibrary

ex = 0
##
# Funkce pro vypsání odmocniny do displeje, je separatne kvůli použití speciálního znaku
# @param ignore mě být ignorován, je tam proto, že bind potřebuje funkce s parametrem

def print_n_root(ignore=0):
    global ex
    gui.display.configure(state='normal')
    gui.display.insert(END,"√")
    gui.display.configure(state='disabled')

##
# Funkce pro vypsání všech potřebných znaků kromě odmocniny do displeje
# @param ignore num představuje znak, který je třeba vypsat

def print_num(num):
    global ex
    if ex == 1:
        gui.display.delete("1.0",END)
        ex = 0
    gui.display.configure(state='normal')
    gui.display.insert(END,num)
    gui.display.configure(state='disabled')

##
# Funkce která načítá vstupy z displeje, následně vypočítává a vrací výsledek do displeje

def execute():
    global ex
    if ex == 1:
        gui.display.delete("1.0",END)
        ex = 0
    gui.display.configure(state = 'normal')
    equation = gui.display.get("1.0",END)
    num = ""
    appended_sign = 0
    arr_inputs = []
    ex = 0
    minus_num=0
    appended_sign_minus=0
    for i in equation:
        if i in ('1','2','3','4','5','6','7','8','9','0'):
            if (appended_sign == 2):
                gui.display.delete("1.0",END)
                gui.display.insert("1.0","Synatax error")
                ex = 1
            appended_sign_minus=0
            appended_sign = 0
            if (minus_num == 1):
                num += '-'
                minus_num=0
            num += i
        else:
            if(i == '-'):
                appended_sign_minus=appended_sign+1
            print(appended_sign, appended_sign_minus)
            if (appended_sign == 1 and not (appended_sign_minus == 1 or appended_sign_minus == 2 )):
                gui.display.delete("1.0",END)
                gui.display.insert("1.0","Synatax error")
                ex = 1
            if num != "" and i != '.':
                arr_inputs.append(num)
            elif num != "" and i == '.':
                num += i
            if i == '-' and num=="" and appended_sign==0:
                print("ggg")
                minus_num=1
                continue
            elif i != '\n' and appended_sign_minus != 2 and i !='.':
                arr_inputs.append(i)
                if (i != '!'):
                    appended_sign=1
                else:
                    appended_sign=2
            if i != '.':
                num=""
            if appended_sign_minus == 2:
                num+='-'

    if ex == 1:
        return
    #factorial
    for i in range(0,len(arr_inputs)):
        print(arr_inputs[i])
    to_delete = []
    for i in range(0,len(arr_inputs)):
        if arr_inputs[i] == '!':
            to_delete.append(i)
            number = int(arr_inputs[i-1])
            arr_inputs[i-1] = math_library.fac(number)
    for i in reversed(to_delete):
        arr_inputs.pop(i)
    to_delete = []
    
    #root
    for i in range(0,len(arr_inputs)):
        if arr_inputs[i] == '√':
            to_delete.append(i)
            to_delete.append(i+1)
            number1 = float(arr_inputs[i-1])
            number2 = float(arr_inputs[i+1])
            arr_inputs[i-1] = math_library.root(number2,number1)
    for i in reversed(to_delete):
        arr_inputs.pop(i)
    to_delete = []

    #pow
    for i in range(0,len(arr_inputs)):
        if arr_inputs[i] == '^':
            to_delete.append(i)
            to_delete.append(i+1)
            number1 = float(arr_inputs[i-1])
            number2 = float(arr_inputs[i+1])
            arr_inputs[i-1] = math_library.mypow(number1,number2)
    for i in reversed(to_delete):
        arr_inputs.pop(i)
    to_delete = []

    #div
    for i in range(0,len(arr_inputs)):
        if arr_inputs[i] == '/':
            to_delete.append(i)
            to_delete.append(i+1)
            number1 = float(arr_inputs[i-1])
            number2 = float(arr_inputs[i+1])
            arr_inputs[i-1] = math_library.div(number1,number2)
    for i in reversed(to_delete):
        arr_inputs.pop(i)
    to_delete = []
    
    #rem
    for i in range(0,len(arr_inputs)):
        if arr_inputs[i] == '/':
            to_delete.append(i)
            to_delete.append(i+1)
            number1 = float(arr_inputs[i-1])
            number2 = float(arr_inputs[i+1])
            arr_inputs[i-1] = math_library.rem(number1,number2)
    for i in reversed(to_delete):
        arr_inputs.pop(i)
    to_delete = []
    #mult
    for i in range(0,len(arr_inputs)):
        if arr_inputs[i] == '*':
            to_delete.append(i)
            to_delete.append(i+1)
            number1 = float(arr_inputs[i-1])
            number2 = float(arr_inputs[i+1])
            arr_inputs[i-1] = math_library.mult(number1,number2)
    for i in reversed(to_delete):
        arr_inputs.pop(i)
    to_delete = []

    #sub
    for i in range(0,len(arr_inputs)):
        if arr_inputs[i] == '-':
            to_delete.append(i)
            to_delete.append(i+1)
            number1 = float(arr_inputs[i-1])
            number2 = float(arr_inputs[i+1])
            arr_inputs[i-1] = math_library.sub(number1,number2)
    for i in reversed(to_delete):
        arr_inputs.pop(i)
    to_delete = []

    #sum
    for i in range(0,len(arr_inputs)):
        if arr_inputs[i] == '+':
            to_delete.append(i)
            to_delete.append(i+1)
            number1 = float(arr_inputs[i-1])
            number2 = float(arr_inputs[i+1])
            arr_inputs[i-1] = math_library.sum(number1,number2)
    for i in reversed(to_delete):
        arr_inputs.pop(i)
    to_delete = []

    gui.display.delete("1.0",END)
    gui.display.insert("1.0",str(arr_inputs[0]))
    gui.display.configure(state='disabled')
        
def del_last_pos(ignore=0):
    gui.display.configure(state='normal')
    gui.display.delete("end-2c")
    gui.display.configure(state='disabled')
def del_all():
    gui.display.configure(state='normal')
    gui.display.delete("1.0",END)
    gui.display.configure(state='disabled')
