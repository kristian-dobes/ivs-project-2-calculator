import tkinter
from sympy import pretty_print
from sympy.abc import a, b, n
from tkinter.tix import *
import executables

def who_knows():
    pass

win = Tk()
win.geometry("390x460")
win.title("Calculator")
canvas = tkinter.Canvas(win)

#creating tooltips
tooltip_plus  = Balloon(win)
tooltip_minus = Balloon(win)
tooltip_mul   = Balloon(win)
tooltip_div   = Balloon(win)
tooltip_pow   = Balloon(win)
tooltip_root  = Balloon(win)
tooltip_del   = Balloon(win)
tooltip_ce    = Balloon(win)
tooltip_fac   = Balloon(win)

display = tkinter.Text(width = 43,height=10)
display.configure(state='disabled')


#creating buttons
    
num1 = tkinter.Button(win,text="1",command=executables.print_1,width=8,height=2)
num2 = tkinter.Button(win,text="2",command=executables.print_2,width=8,height=2)
num3 = tkinter.Button(win,text="3",command=executables.print_3,width=8,height=2)
num4 = tkinter.Button(win,text="4",command=executables.print_4,width=8,height=2)
num5 = tkinter.Button(win,text="5",command=executables.print_5,width=8,height=2)
num6 = tkinter.Button(win,text="6",command=executables.print_6,width=8,height=2)
num7 = tkinter.Button(win,text="7",command=executables.print_7,width=8,height=2)
num8 = tkinter.Button(win,text="8",command=executables.print_8,width=8,height=2)
num9 = tkinter.Button(win,text="9",command=executables.print_9,width=8,height=2)
num0 = tkinter.Button(win,text="0",command=executables.print_0,width=8,height=2)


plus = tkinter.Button(win,text="+",command=executables.print_plus,width=8,height=2)
minus = tkinter.Button(win,text="-",command=executables.print_minus,width=8,height=2)
times = tkinter.Button(win,text="*",command=executables.print_mul,width=8,height=2)

#par_left = tkinter.Button(win,text="(",command=print_lp,width=8,height=2)
#par_right = tkinter.Button(win,text=")",command=print_rp,width=8,height=2)
equals = tkinter.Button(win,text="=",command=executables.execute,width=18,height=5)
division = tkinter.Button(win,text="÷",command=executables.print_div,width=8,height=2)

float_point = tkinter.Button(win,text=",",command=executables.print_dot,width=8,height=2)
ce = tkinter.Button(win,text="CE",command=executables.del_all,width=8,height=2)
delete = tkinter.Button(win,text="⌫",command=executables.del_last_pos,width=8,height=2)

fac = tkinter.Button(win,text="n!",command=executables.print_fac,width=8,height=2)
root = tkinter.Button(win,text="√x",command=executables.print_n_root,width=8,height=2)
tpow = tkinter.Button(win,text="x^n",command=executables.print_n_pow,width=8,height=2)
mod = tkinter.Button(win,text="%",command=executables.print_mod,width=8,height=2)

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


#par_left.place(x=230,y=350)
#par_right.place(x=300,y=350)
equals.place(x=230,y=352)
division.place(x=300,y=250)

win.bind("1", executables.print_1)
win.bind("2", executables.print_2)
win.bind("3", executables.print_3)
win.bind("4", executables.print_4)
win.bind("5", executables.print_5)
win.bind("6", executables.print_6)
win.bind("7", executables.print_7)
win.bind("8", executables.print_8)
win.bind("9", executables.print_9)
win.bind("0", executables.print_0)
win.bind("+", executables.print_plus)
win.bind("-", executables.print_minus)
win.bind("*", executables.print_mul)
win.bind("/", executables.print_div)
win.bind("!", executables.print_fac)


