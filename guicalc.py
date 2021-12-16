from tkinter import *

expression = ""
def onclick(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalbtn():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set(" error ")
        expression = ""
 
def clear():
    global expression
    expression = ""
    equation.set("")
 
if __name__ == "__main__":
    win = Tk()
    win.configure(background="light gray")
    win.title("GUI Calculator")
    win.geometry("280x180")
    equation = StringVar()
    input_field = Entry(win, textvariable=equation)
    input_field.grid(columnspan=4, ipadx=70)
    
    button1 = Button(win, text=' 1 ', fg='black', bg='#d9d9d9', command=lambda: onclick(1), height=1, width=7)
    button1.grid(row=2, column=0)
    button2 = Button(win, text=' 2 ', fg='black', bg='#d9d9d9', command=lambda: onclick(2), height=1, width=7)
    button2.grid(row=2, column=1)
    button3 = Button(win, text=' 3 ', fg='black', bg='#d9d9d9', command=lambda: onclick(3), height=1, width=7)
    button3.grid(row=2, column=2)
    button4 = Button(win, text=' 4 ', fg='black', bg='#d9d9d9', command=lambda: onclick(4), height=1, width=7)
    button4.grid(row=3, column=0)
    button5 = Button(win, text=' 5 ', fg='black', bg='#d9d9d9', command=lambda: onclick(5), height=1, width=7)
    button5.grid(row=3, column=1)
    button6 = Button(win, text=' 6 ', fg='black', bg='#d9d9d9', command=lambda: onclick(6), height=1, width=7)
    button6.grid(row=3, column=2)
    button7 = Button(win, text=' 7 ', fg='black', bg='#d9d9d9', command=lambda: onclick(7), height=1, width=7)
    button7.grid(row=4, column=0)
    button8 = Button(win, text=' 8 ', fg='black', bg='#d9d9d9', command=lambda: onclick(8), height=1, width=7)
    button8.grid(row=4, column=1)
    button9 = Button(win, text=' 9 ', fg='black', bg='#d9d9d9', command=lambda: onclick(9), height=1, width=7)
    button9.grid(row=4, column=2)
    button0 = Button(win, text=' 0 ', fg='black', bg='#d9d9d9', command=lambda: onclick(0), height=1, width=7)
    button0.grid(row=5, column=0)
    btnplus = Button(win, text=' + ', fg='black', bg='#d9d9d9', command=lambda: onclick("+"), height=1, width=7)
    btnplus.grid(row=2, column=3)
    btnminus = Button(win, text=' - ', fg='black', bg='#d9d9d9', command=lambda: onclick("-"), height=1, width=7)
    btnminus.grid(row=3, column=3)
    btnmultiply = Button(win, text=' * ', fg='black', bg='#d9d9d9', command=lambda: onclick("*"), height=1, width=7)
    btnmultiply.grid(row=4, column=3)
    btndivide = Button(win, text=' / ', fg='black', bg='#d9d9d9', command=lambda: onclick("/"), height=1, width=7)
    btndivide.grid(row=5, column=3)
    btnequal = Button(win, text=' = ', fg='black', bg='#d9d9d9', command=equalbtn, height=1, width=7)
    btnequal.grid(row=5, column=2)
    btnclear = Button(win, text='Clear', fg='black', bg='#d9d9d9', command=clear, height=1, width=7)
    btnclear.grid(row=5, column='1')
    btnDecimal= Button(win, text='.', fg='black', bg='#d9d9d9', command=lambda: onclick('.'), height=1, width=7)
    btnDecimal.grid(row=6, column=0)
    
    win.mainloop()