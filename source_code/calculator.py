from tkinter import *
import tkinter.font as font
from fractions import Fraction
import re

langs=['EN', 'PT']

class Result:
    def __init__(self, window):
        self.value=0
        self.y2=Label(window, text='X', font=answer_font)
        self.y2.grid(row=4, column=4)
        window.after(50, self.refreshLabel)
        
    def rule_of_three(self, x1, x2, y1):
        try:
            x1, x2, y1 = float(x1), float(x2), float(y1)
            y2=round((x2*y1)/x1, 5)
            if y2.is_integer():
                return int(y2)
            else:
                return y2
        except:
            return 'X'
        
    def refreshLabel(self):
        global x1, x2, y1
        
        self.x1_value=x1.get()
        self.x2_value=x2.get()
        self.y1_value=y1.get()
        
        self.isNumber()
        self.fractionToFloat()
        
        self.value=self.rule_of_three(self.x1_value, self.x2_value, self.y1_value)
        
        self.y2.config(text=self.value)
        
        window.after(50, self.refreshLabel)
        
    def fractionToFloat(self):
        try:
            self.values=self.x1_value.split('/')
            self.isfraction=len(self.values) == 2 and all(i.isdigit() for i in self.values)
            if self.isfraction==True:
                self.x1_value=Fraction(self.x1_value)
        except:
            self.x1_value=''
            
        try:
            self.values=self.x2_value.split('/')
            self.isfraction=len(self.values) == 2 and all(i.isdigit() for i in self.values)
            if self.isfraction==True:
                self.x2_value=Fraction(self.x2_value)
        except:
            self.x2_value=''
            
        try:
            self.values=self.y1_value.split('/')
            self.isfraction=len(self.values) == 2 and all(i.isdigit() for i in self.values)
            if self.isfraction==True:
                self.y1_value=Fraction(self.y1_value)
        except:
            self.y1_value=''
        
    def isNumber(self):
        try:
            self.x1_try=float(self.x1_value)
        except:
            self.x1_value=''
            
        try:
            self.x2_try=float(self.x2_value)
        except:
            self.x2_value=''
            
        try:
            self.y1_try=float(self.y1_value)
        except:
            self.y1_value=''

if __name__=='__main__':
    window = Tk()
    window.resizable(False, False)
    window.title("Rule of three calculator")
    
    default_font=font.Font(family='Calibri')
    answer_font=font.Font(family='Calibri', weight='bold')

    blankColumn1=Label(window, text="           ")
    blankColumn2=Label(window, text="           ")
    blankRow1=Label(window, text="           ")
    blankRow2=Label(window, text="           ")
    blankSpace1=Label(window, text="           ")
    blankSpace2=Label(window, text="           ")

    x1=Entry(window, font=default_font, justify='center')
    x2=Entry(window, font=default_font, justify='center')
    y1=Entry(window, font=default_font, justify='center')

    isToUpper=Label(window, text="is to", font=default_font)
    asIs=Label(window, text="as", font=default_font)
    isToLower=Label(window, text="is to", font=default_font)

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
    
    result=Result(window)

    window.mainloop()