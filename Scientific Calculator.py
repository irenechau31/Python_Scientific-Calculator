import tkinter as tk
import math
from tkinter import Frame, Button, Label

class Scientific_Calculator: 
    def __init__(self, root):
        self.root = root
        self.root.title("VS Code Calculator")
        self.root.geometry("356x530+400+70")

        self.MainFrame = Frame(self.root, bd =18, width = 40, height = 680, relief = 'ridge', bg = 'powder blue')
        self.MainFrame.grid()
        self.WidgetFrame=Frame(self.MainFrame, bd = 18, width=30, height = 670, relief = 'ridge', bg ='cadet blue')
        self.WidgetFrame.grid()

        self.lblDisplay = Label(self.WidgetFrame, width = 8, height = 1, bg = 'white', font =('arial', 35, 'bold'))
        self.lblDisplay.grid(row=0, column =0, columnspan =4, padx =10, pady =10)

        self.input_button =""
    # 1ST ROW
        self.create_button("<-", 1, 0)
        self.create_button("CE", 1, 1)
        self.create_button("C", 1, 2)
        self.create_button("+/-", 1, 3)
    #2ND ROW
        self.create_button("7", 2, 0)
        self.create_button("8", 2, 1)
        self.create_button("9", 2, 2)
        self.create_button("+", 2, 3)
    #3ND ROW
        self.create_button("4", 3, 0)
        self.create_button("5", 3, 1)
        self.create_button("6", 3, 2)
        self.create_button("-", 3, 3)
    #4ND ROW
        self.create_button("1", 4, 0)
        self.create_button("2", 4, 1)
        self.create_button("3", 4, 2)
        self.create_button("*", 4, 3)
    #5ND ROW
        self.create_button("0", 5, 0)
        self.create_button(".", 5, 1)
        self.create_button("=", 5, 2)
        self.create_button("/", 5, 3)

    def create_button(self, text, row, column):
        button_widget = Button(self.WidgetFrame, text=text,width = 4, height =1, bg ='powder blue', font = ('arial', 15, 'bold'), command =lambda:self.button_click(text))
        button_widget.grid(row=row, column=column, padx =4, pady=4)

    def button_click (self, text):
        if text == '<-':
            self.input_button = self.input_button[:-1]
        elif text == 'CE':
            self.input_button =""
        elif text == 'C':
            self.input_button =""

        elif text == '=':
            try:
                self.input_button =str(eval(self.input_button))
            except:
                self.input_button ='error'
        elif text =="+/-":
            self.input_button = str(float(self.input_button))
        else:
            self.input_button += text
        self.lblDisplay.config(text=self.input_button)

root = tk.Tk()
app = Scientific_Calculator(root)
root.mainloop()