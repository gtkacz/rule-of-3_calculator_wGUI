from tkinter import *

langs=['EN', 'PT']

def rule_of_three(x1, x2, y1):
    return (x2*y1)/x1

window = Tk()
window.title("Rule of three calculator")

n=[5, 5]

blankColumn1=Label(window, text="           ")
blankColumn2=Label(window, text="           ")
blankRow1=Label(window, text="           ")
blankRow2=Label(window, text="           ")
blankSpace1=Label(window, text="           ")
blankSpace2=Label(window, text="           ")

x1=(Entry(window))
x2=(Entry(window))
y1=(Entry(window))
y2=Label(window, text='x')

def calculate():
    global y2
    
    x1_value=int(x1.get())
    x2_value=int(x2.get())
    y1_value=int(y1.get())
    y2_value=rule_of_three(x1_value, x2_value, y1_value)

    y2.config(text=y2_value)

isToUpper=Label(window, text="is to")
asIs=Label(window, text="as")
isToLower=Label(window, text="is to")

# for row in range(n[0]):
#     Label(window, text="           ").grid(row=row, column=0)
    
# for column in range(n[1]):
#     Label(window, text="           ").grid(row=0, column=column)

blankColumn1.grid(row=0, column=0, rowspan=5)
blankColumn2.grid(row=0, column=5, rowspan=5)
blankRow1.grid(row=0, column=1, columnspan=3)
blankRow2.grid(row=5, column=1, columnspan=3)
#blankSpace1.grid(row=2, column=2)
#blankSpace2.grid(row=2, column=2)

x1.grid(row=2, column=2, padx=25, pady=10)
x2.grid(row=2, column=4, padx=25, pady=10)
y1.grid(row=4, column=2, padx=25, pady=10)
y2.grid(row=4, column=4)

isToUpper.grid(row=2, column=3)
asIs.grid(row=3, column=3)
isToLower.grid(row=4, column=3)

x1.insert(0, '1')
x2.insert(0, '1')
y1.insert(0, '1')

window.after(500, calculate())

window.mainloop()