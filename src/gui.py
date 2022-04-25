import tkinter
from tkinter.tix import *
import executables

win = Tk()
#############################################################################################################
# Název projektu: Matematická kalkulačka
# Soubor: mathlibrary.py
# Datum: 10.4.2022
# Poslední změna: 24.4.2022
# Autoři: Miroslav Bálek (xbalek02), Kristián Dobeš (xdobes22), Maroš Synák (xsynak03), Jan Král (xkralj12)
#
# modul pro grafické uživatelské rozhraní včetně všech čísel a symbolů nezbytných pro matematickou knihovnu
# a jejich zobrazení
#############################################################################################################

##
# @file guy.py
#
# @brief Matematická knihovna
#
# @author Miroslav Bálek (xbalek02), Kristián Dobeš (xdobes22), Maroš Synák (xsynak03), Jan Král (xkralj12)
# 
#
# @section DESCRIPTION
#
# modul pro grafické uživatelské rozhraní včetně všech čísel a symbolů nezbytných pro matematickou knihovnu
# a jejich zobrazení

# creating base for calculator
win.geometry("390x460")
win.title("Calculator")
canvas = tkinter.Canvas(win)

# creating tooltips
tooltip_plus  = Balloon(win)
tooltip_minus = Balloon(win)
tooltip_mul   = Balloon(win)
tooltip_div   = Balloon(win)
tooltip_pow   = Balloon(win)
tooltip_root  = Balloon(win)
tooltip_del   = Balloon(win)
tooltip_ce    = Balloon(win)
tooltip_fac   = Balloon(win)

# creating display
display = tkinter.Text(width = 43,height=10)
display.configure(state='disabled')


#creating buttons
    
num1 = tkinter.Button(win,text="1",command=lambda: executables.print_num('1'),width=8,height=2)
num2 = tkinter.Button(win,text="2",command=lambda: executables.print_num('2'),width=8,height=2)
num3 = tkinter.Button(win,text="3",command=lambda: executables.print_num('3'),width=8,height=2)
num4 = tkinter.Button(win,text="4",command=lambda: executables.print_num('4'),width=8,height=2)
num5 = tkinter.Button(win,text="5",command=lambda: executables.print_num('5'),width=8,height=2)
num6 = tkinter.Button(win,text="6",command=lambda: executables.print_num('6'),width=8,height=2)
num7 = tkinter.Button(win,text="7",command=lambda: executables.print_num('7'),width=8,height=2)
num8 = tkinter.Button(win,text="8",command=lambda: executables.print_num('8'),width=8,height=2)
num9 = tkinter.Button(win,text="9",command=lambda: executables.print_num('9'),width=8,height=2)
num0 = tkinter.Button(win,text="0",command=lambda: executables.print_num('0'),width=8,height=2)

plus = tkinter.Button(win,text="+",command=lambda: executables.print_num('+'),width=8,height=2)
minus = tkinter.Button(win,text="-",command=lambda: executables.print_num('-'),width=8,height=2)
times = tkinter.Button(win,text="*",command=lambda: executables.print_num('*'),width=8,height=2)
division = tkinter.Button(win,text="÷",command=lambda: executables.print_num('/'),width=8,height=2)

float_point = tkinter.Button(win,text=".",command=lambda: executables.print_num('.'),width=8,height=2)

ce = tkinter.Button(win,text="CE",command=executables.del_all,width=8,height=2)
delete = tkinter.Button(win,text="⌫",command=executables.del_last_pos,width=8,height=2)

fac = tkinter.Button(win,text="n!",command=lambda: executables.print_num('!'),width=8,height=2)
root = tkinter.Button(win,text="√x",command=executables.print_n_root,width=8,height=2)
tpow = tkinter.Button(win,text="x^n",command=lambda: executables.print_num('^'),width=8,height=2)
mod = tkinter.Button(win,text="%",command=lambda: executables.print_num('%'),width=8,height=2)

equals = tkinter.Button(win,text="=",command=executables.execute,width=18,height=5)

#binding tooltips to buttons and setting messages
tooltip_plus.bind_widget(plus, balloonmsg="place inbetween 2 expressions for addition")
tooltip_minus.bind_widget(minus, balloonmsg="place inbetween 2 expressions for substraction")
tooltip_mul.bind_widget(times, balloonmsg="place inbetween 2 expressions for multiplication")
tooltip_div.bind_widget(division, balloonmsg="place inbetween 2 expressions for division")
tooltip_del.bind_widget(delete, balloonmsg="deletes last character")
tooltip_ce.bind_widget(ce, balloonmsg="clears all")
tooltip_fac.bind_widget(fac, balloonmsg="place after an expression for factorial")
tooltip_root.bind_widget(root, balloonmsg="place before an expression for root of n")
tooltip_pow.bind_widget(tpow, balloonmsg="place after an expression for pow to the power of n")


#placing buttons

display.place(x=19,y=20)

num1.place(x=20,y=350)
num4.place(x=20,y=300)
num7.place(x=20,y=250)
num2.place(x=90,y=350)
num5.place(x=90,y=300)
num8.place(x=90,y=250)
num3.place(x=160,y=350)
num6.place(x=160,y=300)
num9.place(x=160,y=250)

fac.place(x=20,y=200)
root.place(x=90,y=200)
tpow.place(x=160,y=200)
mod.place(x=160,y=400)

plus.place(x=300,y=300)
minus.place(x=230,y=300)
times.place(x=230,y=250)

num0.place(x=20,y=400)
float_point.place(x=90,y=400)
delete.place(x=230,y=200)
ce.place(x=300,y=200)
equals.place(x=230,y=352)
division.place(x=300,y=250)

# binding keyboard to buttons
win.bind("1", lambda event:executables.print_num('1'))
win.bind("2", lambda event:executables.print_num('2'))
win.bind("3", lambda event:executables.print_num('3'))
win.bind("4", lambda event:executables.print_num('4'))
win.bind("5", lambda event:executables.print_num('5'))
win.bind("6", lambda event:executables.print_num('6'))
win.bind("7", lambda event:executables.print_num('7'))
win.bind("8", lambda event:executables.print_num('8'))
win.bind("9", lambda event:executables.print_num('9'))
win.bind("0", lambda event:executables.print_num('0'))
win.bind("+", lambda event:executables.print_num('+'))
win.bind("-", lambda event:executables.print_num('-'))
win.bind("*", lambda event:executables.print_num('*'))
win.bind("/", lambda event:executables.print_num('/'))
win.bind("!", lambda event:executables.print_num('!'))
win.bind("%", lambda event:executables.print_num('%'))
win.bind("^", lambda event:executables.print_num('^'))
win.bind(".", lambda event:executables.print_num('.'))

win.mainloop()