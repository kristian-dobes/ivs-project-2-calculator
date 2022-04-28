#############################################################################################################
# Název projektu: Matematická kalkulačka
# Soubor: executables.py
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
# @brief Integračny modul
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
#from tkinter.tix import *
import mathlibrary

## global variable if 1 means to delete screen on new input
ex = 0
##
# Funkce pro vypsání odmocniny do displeje, je separatne kvůli použití speciálního znaku
# @param ignore mě být ignorován, je tam proto, že bind potřebuje funkce s parametrem

def print_n_root(ignore=0):
    global ex
    gui.display.configure(state='normal')
    gui.display.insert(tkinter.END,"√")
    gui.display.configure(state='disabled')

##
# Funkce pro vypsání všech potřebných znaků kromě odmocniny do displeje
# @param ignore num představuje znak, který je třeba vypsat

def print_num(num):
    global ex
    if ex == 1:
        gui.display.delete("1.0",tkinter.END)
        ex = 0
    gui.display.configure(state='normal')
    gui.display.insert(tkinter.END,num)
    gui.display.configure(state='disabled')

##
# Funkce která načítá vstupy z displeje, následně vypočítává a vrací výsledek do displeje

def execute():
    global ex
    if ex == 1:
        gui.display.delete("1.0",tkinter.END)
        ex = 0
    gui.display.configure(state = 'normal')
    equation = gui.display.get("1.0",tkinter.END)

    ## do tohoto se načítají číslice, dokud nevytvoří celé číslo
    num = ""
    appended_sign = 0 ## pokud poslední přečtený znak není číselný
    arr_inputs = [] ## array of inputs separated into numbers and characters
    ex = 0 ## if 1 next input will clear the display
    minus_num = 0 ## if number is negative
    appended_sign_minus = 0 ## count of minus signs
    for i in equation:
        if i in ('1','2','3','4','5','6','7','8','9','0'): ## if char in input is digit
            if (appended_sign == 2): ## if 2 operations have been loaded in a row throw syntax error
                gui.display.delete("1.0",tkinter.END)
                gui.display.insert("1.0","Synatax error")
                ex = 1
            appended_sign_minus=0 ## resets to 0
            appended_sign = 0 ## resets to 0
            if (minus_num == 1): ## if number is negative resets it
                num += '-'
                minus_num = 0
            num += i
        else:
            if(i == '-'):
                appended_sign_minus=appended_sign+1
            elif i != '-':
                appended_sign_minus=0
            if (appended_sign == 1 and not (appended_sign_minus == 1 or appended_sign_minus == 2 )):
                gui.display.delete("1.0",tkinter.END)
                gui.display.insert("1.0","Synatax error")
                ex = 1
            if i == '!':
                for digit in num:
                    if digit == '.':
                        gui.display.delete("1.0",tkinter.END)
                        gui.display.insert("1.0","Synatax error")
                        ex = 1
            if i == '.':
                for digit in num:
                    if digit == '.':
                        gui.display.delete("1.0",tkinter.END)
                        gui.display.insert("1.0","Synatax error")
                        ex = 1
            if num != "" and i != '.':
                arr_inputs.append(num)
            elif num != "" and i == '.':
                num += i
            if i == '-' and num=="" and appended_sign==0:
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
    to_delete = [] # contains indexes of elements in arr_inputs to be deleted
    for i in range(0,len(arr_inputs)):
        if arr_inputs[i] == '!':
            to_delete.append(i) # adds number to be deleted
            number = int(arr_inputs[i-1]) # factorial of this number is to be calculated
            arr_inputs[i-1] = mathlibrary.fac(number) # saves 
    for i in reversed(to_delete): # deletes numbers from arr that are redundent
        arr_inputs.pop(i)
    to_delete = []
    
    #root
    for i in range(0,len(arr_inputs)):
        if arr_inputs[i] == '√':
            to_delete.append(i)
            to_delete.append(i+1)
            number1 = float(arr_inputs[i-1])
            number2 = float(arr_inputs[i+1])
            arr_inputs[i-1] = mathlibrary.root(number2,number1)
            out = mathlibrary.root(number1,number2)
            arr_inputs[i+1] = mathlibrary.root(number1,number2)
    for i in reversed(to_delete):
        arr_inputs[i-1] = out
        arr_inputs.pop(i)
    to_delete = []

    #mypow
    for i in range(0,len(arr_inputs)):
        if arr_inputs[i] == '^':
            to_delete.append(i)
            to_delete.append(i+1)
            number1 = float(arr_inputs[i-1])
            number2 = float(arr_inputs[i+1])
            arr_inputs[i-1] = mathlibrary.mypow(number1,number2)
            out = mathlibrary.mypow(number1,number2)
            arr_inputs[i+1] = mathlibrary.mypow(number1,number2)
    for i in reversed(to_delete):
        arr_inputs[i-1] = out
        arr_inputs.pop(i)
    to_delete = []

    #div
    for i in range(0,len(arr_inputs)):
        if arr_inputs[i] == '/':
            to_delete.append(i)
            to_delete.append(i+1)
            number1 = float(arr_inputs[i-1])
            number2 = float(arr_inputs[i+1])
            arr_inputs[i-1] = mathlibrary.div(number1,number2)
            out = mathlibrary.div(number1,number2)
            arr_inputs[i+1] = mathlibrary.div(number1,number2)
    for i in reversed(to_delete):
        arr_inputs[i-1] = out
        arr_inputs.pop(i)
    to_delete = []
    
    #rem
    for i in range(0,len(arr_inputs)):
        if arr_inputs[i] == '/':
            to_delete.append(i)
            to_delete.append(i+1)
            number1 = float(arr_inputs[i-1])
            number2 = float(arr_inputs[i+1])
            arr_inputs[i-1] = mathlibrary.rem(number1,number2)
            out = mathlibrary.rem(number1,number2)
            arr_inputs[i+1] = mathlibrary.rem(number1,number2)
    for i in reversed(to_delete):
        arr_inputs[i-1] = out
        arr_inputs.pop(i)
    to_delete = []
    #mult
    for i in range(0,len(arr_inputs)):
        if arr_inputs[i] == '*':
            to_delete.append(i)
            to_delete.append(i+1)
            number1 = float(arr_inputs[i-1])
            number2 = float(arr_inputs[i+1])
            arr_inputs[i-1] = mathlibrary.mult(number1,number2)
            out = mathlibrary.mult(number1,number2)
            arr_inputs[i+1] = mathlibrary.mult(number1,number2)
    for i in reversed(to_delete):
        arr_inputs[i-1] = out
        arr_inputs.pop(i)
    to_delete = []

    #sub
    for i in range(0,len(arr_inputs)):
        if arr_inputs[i] == '-':
            to_delete.append(i)
            to_delete.append(i+1)
            number1 = float(arr_inputs[i-1])
            number2 = float(arr_inputs[i+1])
            arr_inputs[i-1] = mathlibrary.sub(number1,number2)
            out = mathlibrary.sub(number1,number2)
            arr_inputs[i+1] = mathlibrary.sub(number1,number2)
    for i in reversed(to_delete):
        arr_inputs[i-1] = out
        arr_inputs.pop(i)
    to_delete = []
    #sum
    for i in range(0,len(arr_inputs)):
        if arr_inputs[i] == '+':
            to_delete.append(i)
            to_delete.append(i+1)
            number1 = float(arr_inputs[i-1])
            number2 = float(arr_inputs[i+1])
            arr_inputs[i-1] = mathlibrary.sum(number1,number2)
            out = mathlibrary.sum(number1,number2)
            arr_inputs[i+1] = mathlibrary.sum(number1,number2)
    for i in reversed(to_delete):
        arr_inputs[i-1] = out
        arr_inputs.pop(i)
    to_delete = []

    gui.display.delete("1.0",tkinter.END)
    gui.display.insert("1.0",str(arr_inputs[0]))
    gui.display.configure(state='disabled')
        
def del_last_pos(ignore=0):
    gui.display.configure(state='normal')
    gui.display.delete("end-2c")
    gui.display.configure(state='disabled')
def del_all():
    gui.display.configure(state='normal')
    gui.display.delete("1.0",tkinter.END)
    gui.display.configure(state='disabled')

def help_in():
    gui.num1.place_forget()
    gui.num2.place_forget()
    gui.num3.place_forget()
    gui.num4.place_forget()
    gui.num5.place_forget()
    gui.num6.place_forget()
    gui.num7.place_forget()
    gui.num8.place_forget()
    gui.num9.place_forget()
    gui.num0.place_forget()
    gui.plus.place_forget()
    gui.minus.place_forget()
    gui.times.place_forget()
    gui.division.place_forget()
    gui.fac.place_forget()
    gui.root.place_forget()
    gui.tpow.place_forget()
    gui.delete.place_forget()
    gui.ce.place_forget()
    gui.float_point.place_forget()
    gui.mod.place_forget()
    gui.equals.place_forget()
    gui.display.place_forget()
    gui.help_in.place_forget()

    gui.help_out.place(x=0,y=0)
    text = gui.canvas.create_text(5,50,text="+", anchor=tkinter.W)
    text = gui.canvas.create_text(20,50,text= ":adds 2 numbers format(num1+num2)", anchor=tkinter.W)
    text = gui.canvas.create_text(5,75,text= "-",anchor=tkinter.W)
    text = gui.canvas.create_text(20,75,text= ":substracts 2 numbers format(num1-num2)", anchor=tkinter.W)
    text = gui.canvas.create_text(5,100,text= "/", anchor=tkinter.W)
    text = gui.canvas.create_text(20,100,text= ":divides 2 numbers format(num1/num2)", anchor=tkinter.W)
    text = gui.canvas.create_text(5,125,text= "*", anchor=tkinter.W)
    text = gui.canvas.create_text(20,125,text= ":multiplies 2 numbers format(num1*num2)", anchor=tkinter.W)
    text = gui.canvas.create_text(5,150,text= "%", anchor=tkinter.W)
    text = gui.canvas.create_text(20,150,text= ":modulos 2 numbers format(num1%num2)", anchor=tkinter.W)
    text = gui.canvas.create_text(5,175,text= "^", anchor=tkinter.W)
    text = gui.canvas.create_text(20,175,text= ":num x to the mypower of num2 format(num1^num2)", anchor=tkinter.W)
    text = gui.canvas.create_text(5,200,text= "!", anchor=tkinter.W)
    text = gui.canvas.create_text(20,200,text= ":factorial of n format(n!) , max value of n 170", anchor=tkinter.W)
    text = gui.canvas.create_text(5,225,text= "√", anchor=tkinter.W)
    text = gui.canvas.create_text(20,225,text= ":nth root of x format(n√x)", anchor=tkinter.W)
    text = gui.canvas.create_text(5,250,text= ".", anchor=tkinter.W)
    text = gui.canvas.create_text(20,250,text= ":floating point (whole_num.float_num)", anchor=tkinter.W)
   
    gui.canvas.pack()

def help_out():
    gui.display.place(x=19,y=30)
    gui.num1.place(x=20,y=360)
    gui.num4.place(x=20,y=310)
    gui.num7.place(x=20,y=260)
    gui.num2.place(x=90,y=360)
    gui.num5.place(x=90,y=310)
    gui.num8.place(x=90,y=260)
    gui.num3.place(x=160,y=360)
    gui.num6.place(x=160,y=310)
    gui.num9.place(x=160,y=260)

    gui.fac.place(x=20,y=210)
    gui.root.place(x=90,y=210)
    gui.tpow.place(x=160,y=210)
    gui.mod.place(x=160,y=410)

    gui.plus.place(x=300,y=310)
    gui.minus.place(x=230,y=310)
    gui.times.place(x=230,y=260)

    gui.num0.place(x=20,y=410)
    gui.float_point.place(x=90,y=410)
    gui.delete.place(x=230,y=210)
    gui.ce.place(x=300,y=210)
    gui.equals.place(x=230,y=362)
    gui.division.place(x=300,y=260)
    gui.help_out.place_forget()
    gui.canvas.pack_forget()
    gui.help_in.place(x=0,y=0)

