from tkinter import *
window = Tk()
window.geometry('400x300+400+200')
window.title('Simple Calculetor')
window.resizable(0,0)
window.configure(bg = '#455a64')
###########################################
total = StringVar()
first = StringVar()
second = StringVar()
def add_plus():
    total.set('+')

def add_min():
    total.set('-')

def add_mult():
    total.set('*')

def add_div():
    total.set('/')

def sum_():
    try:
        if total.get()=="+":
            total.set(int(first.get())+int(second.get()))
            first.set('')
            second.set('')
        elif total.get()=="-":
            total.set(int(first.get())-int(second.get()))
            first.set('')
            second.set('')
        elif total.get()=="*":
            total.set(int(first.get())*int(second.get()))
            first.set('')
            second.set('')
        elif total.get()=="/":
            total.set(int(first.get())//int(second.get()))
            first.set('')
            second.set('')
    except Exception:
            pass
###########################################
lbf = Label(window, text = 'First',
            bg = '#455a64',
            fg = 'white',
            bd = 4,
            font=('arial', 10, 'bold')
            )
lbs = Label(window, text = 'Second',
            bg = '#455a64',
            fg = 'white',
            bd = 4,
            font=('arial', 10, 'bold')
            )
lbt = Label(window, text = 'Total',
            bg = '#455a64',
            fg = 'white',
            bd = 4,
            font=('arial', 10, 'bold')
            )
###################################################
entf = Entry(window, width=40,
             bd = 4,
             fg = 'black',
             textvariable = first
             )
ents = Entry(window, width=40,
             bd = 4,
             fg = 'black',
             textvariable = second
             )
entt = Entry(window, width=40,
             bd = 4,
             fg = 'black',
             textvariable = total
             )
###################################################
btsum = Button(window, text = 'sum',
               width=5,
               height=2,
               bd = 4,
               fg = 'black',
               font=('arial', 10, 'bold'),
               command = sum_
               )
btplus = Button(window, text = '+',
                width=5,
                height=2,
                bd = 4,
                fg = 'black',
                font=('arial', 10, 'bold'),
                command = add_plus
                )
btmin = Button(window, text = '-',
               width=5,
               height=2,
               bd = 4,
               fg = 'black',
               font=('arial', 10, 'bold'),
               command = add_min
               )
btmult = Button(window, text = 'x',
                width=5,
                height=2,
                bd = 4,
                fg = 'black',
                font=('arial', 10, 'bold'),
                command = add_mult
                )
btdiv = Button(window, text = '/',
               width=5,
               height=2,
               bd = 4,
               fg = 'black',
               font=('arial', 10, 'bold'),
               command = add_div
               )
######################################################

lbf.place(x = 10, y = 15)
lbs.place(x = 10, y = 75)
lbt.place(x = 10, y = 185)
entf.place(x = 80, y = 19)
ents.place(x = 80, y = 75)
entt.place(x = 80, y = 187)
btsum.place(x = 180, y = 230)
btplus.place(x = 110, y = 120)
btmin.place(x = 160, y = 120)
btmult.place(x = 210, y = 120)
btdiv.place(x = 260, y = 120)


window.mainloop()
