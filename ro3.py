from tkinter import *

langs=['EN', 'PT']

def rule_of_three(x1, x2, y1):
    return (x2*y1)/x1

window = Tk()

n=[5, 5]

x1=Entry(window)
x2=Entry(window)
y1=Entry(window)

def click():
    x1_value=int(x1.get())
    x2_value=int(x2.get())
    y1_value=int(y1.get())
    y2_value=rule_of_three(x1_value, x2_value, y1_value)

    y2=Label(window, text=y2_value)
    y2.grid(row=4, column=4)

isToUpper=Label(window, text="is to")
asIs=Label(window, text="as")
isToLower=Label(window, text="is to")

# for row in range(n[0]):
#     Label(window, text="           ").grid(row=row, column=0)
    
# for column in range(n[1]):
#     Label(window, text="           ").grid(row=0, column=column)


x1.grid(row=2, column=2)
x2.grid(row=2, column=4)
y1.grid(row=4, column=2)
#y2.grid(row=4, column=4)

isToUpper.grid(row=2, column=3)
asIs.grid(row=3, column=3)
isToLower.grid(row=4, column=3)

window.mainloop()