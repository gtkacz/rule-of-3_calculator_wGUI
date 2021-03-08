from tkinter import *

langs=['EN', 'PT']

def rule_of_three(x1, x2, y1):
    return (x2*y1)/x1

class Result:
    def __init__(self, window):
        self.value=0
        self.y2=Label(window, text='x')
        self.y2.grid(row=4, column=4)
        window.after(500, self.refreshLabel)
        
    def refreshLabel(self):
        global x1, x2, y1
        
        x1_value=int(x1.get())
        x2_value=int(x2.get())
        y1_value=int(y1.get())
        
        self.value=rule_of_three(x1_value, x2_value, y1_value)
        
        self.y2.config(text=self.value)
        
        window.after(500, self.refreshLabel)

if __name__=='__main__':
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

    isToUpper=Label(window, text="is to")
    asIs=Label(window, text="as")
    isToLower=Label(window, text="is to")

    blankColumn1.grid(row=0, column=0, rowspan=5)
    blankColumn2.grid(row=0, column=5, rowspan=5)
    blankRow1.grid(row=0, column=1, columnspan=3)
    blankRow2.grid(row=5, column=1, columnspan=3)

    x1.grid(row=2, column=2, padx=25, pady=10)
    x2.grid(row=2, column=4, padx=25, pady=10)
    y1.grid(row=4, column=2, padx=25, pady=10)

    isToUpper.grid(row=2, column=3)
    asIs.grid(row=3, column=3)
    isToLower.grid(row=4, column=3)

    x1.insert(0, '1')
    x2.insert(0, '1')
    y1.insert(0, '1')
    
    result=Result(window)

    window.mainloop()