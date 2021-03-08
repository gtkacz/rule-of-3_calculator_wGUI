from tkinter import *

langs=['EN', 'PT']

def rule_of_three(x1, x2, y1):
    if x1!=0 and (type(x1)!=None) and (x1!='' and x2!='' and y1!=''):
        x1, x2, y1 = int(x1), int(x2), int(y1)
        return (x2*y1)/x1
    else:
        return 'X'

class Result:
    def __init__(self, window):
        self.value=0
        self.y2=Label(window, text='X')
        self.y2.grid(row=4, column=4)
        window.after(50, self.refreshLabel)
        
    def refreshLabel(self):
        global x1, x2, y1
        
        self.x1_value=x1.get()
        self.x2_value=x2.get()
        self.y1_value=y1.get()
        
        self.isNumber()
        
        self.value=rule_of_three(self.x1_value, self.x2_value, self.y1_value)
        
        self.y2.config(text=self.value)
        
        window.after(50, self.refreshLabel)
        
    def isNumber(self):
        try:
            self.x1_try=int(self.x1_value)
        except:
            self.x1_value=''
            
        try:
            self.x2_try=int(self.x2_value)
        except:
            self.x2_value=''
            
        try:
            self.y1_try=int(self.y1_value)
        except:
            self.y1_value=''

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

    x1=Entry(window)
    x2=Entry(window)
    y1=Entry(window)

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

    #x1.insert(0, '1')
    #x2.insert(0, '1')
    #y1.insert(0, '1')
    
    result=Result(window)

    window.mainloop()