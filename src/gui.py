import tkinter
#from tkinter.tix import *
import executables

win = tkinter.Tk()
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
win.geometry("390x470")
win.title("Calculator")
canvas = tkinter.Canvas(win)


# creating display
display = tkinter.Text(width = 43,height=10)
display.configure(state='disabled')

#creating help button
help_in = tkinter.Button(win,text="?",command=lambda: executables.help_in(),width=1,height=1)
help_out = tkinter.Button(win,text="?",command=lambda: executables.help_out(),width=1,height=1)

#creating buttons
    
num1 = tkinter.Button(win,text="1",command=lambda: executables.print_num('1'),width=5,height=2)
num2 = tkinter.Button(win,text="2",command=lambda: executables.print_num('2'),width=5,height=2)
num3 = tkinter.Button(win,text="3",command=lambda: executables.print_num('3'),width=5,height=2)
num4 = tkinter.Button(win,text="4",command=lambda: executables.print_num('4'),width=5,height=2)
num5 = tkinter.Button(win,text="5",command=lambda: executables.print_num('5'),width=5,height=2)
num6 = tkinter.Button(win,text="6",command=lambda: executables.print_num('6'),width=5,height=2)
num7 = tkinter.Button(win,text="7",command=lambda: executables.print_num('7'),width=5,height=2)
num8 = tkinter.Button(win,text="8",command=lambda: executables.print_num('8'),width=5,height=2)
num9 = tkinter.Button(win,text="9",command=lambda: executables.print_num('9'),width=5,height=2)
num0 = tkinter.Button(win,text="0",command=lambda: executables.print_num('0'),width=5,height=2)

plus = tkinter.Button(win,text="+",command=lambda: executables.print_num('+'),width=5,height=2)
minus = tkinter.Button(win,text="-",command=lambda: executables.print_num('-'),width=5,height=2)
times = tkinter.Button(win,text="*",command=lambda: executables.print_num('*'),width=5,height=2)
division = tkinter.Button(win,text="÷",command=lambda: executables.print_num('/'),width=5,height=2)

float_point = tkinter.Button(win,text=".",command=lambda: executables.print_num('.'),width=5,height=2)

ce = tkinter.Button(win,text="CE",command=executables.del_all,width=5,height=2)
delete = tkinter.Button(win,text="⌫",command=executables.del_last_pos,width=5,height=2)

fac = tkinter.Button(win,text="n!",command=lambda: executables.print_num('!'),width=5,height=2)
root = tkinter.Button(win,text="n√x",command=executables.print_n_root,width=5,height=2)
tpow = tkinter.Button(win,text="x^n",command=lambda: executables.print_num('^'),width=5,height=2)
mod = tkinter.Button(win,text="%",command=lambda: executables.print_num('%'),width=5,height=2)

equals = tkinter.Button(win,text="=",command=executables.execute,width=14,height=5)


#placing buttons

display.place(x=19,y=30)

num1.place(x=20,y=360)
num4.place(x=20,y=310)
num7.place(x=20,y=260)
num2.place(x=90,y=360)
num5.place(x=90,y=310)
num8.place(x=90,y=260)
num3.place(x=160,y=360)
num6.place(x=160,y=310)
num9.place(x=160,y=260)

fac.place(x=20,y=210)
root.place(x=90,y=210)
tpow.place(x=160,y=210)
mod.place(x=160,y=410)

plus.place(x=300,y=310)
minus.place(x=230,y=310)
times.place(x=230,y=260)

num0.place(x=20,y=410)
float_point.place(x=90,y=410)
delete.place(x=230,y=210)
ce.place(x=300,y=210)
equals.place(x=230,y=362)
division.place(x=300,y=260)

help_in.place(x=0,y=0)

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
