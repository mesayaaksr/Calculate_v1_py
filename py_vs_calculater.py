from tkinter import*


class Calculator:
    
    def __init__(self, root):
        
        self.root = root
        self.root .title("Calculator")
        self.root.geometry("600x680+400+100")
        self.root.configure(bg = 'cadet blue')

        
        self.MainFrame = Frame(self.root,bd=18,width=600,height=670, relief=RIDGE, bg = 'powder blue')
        self.MainFrame.grid()
        self.WidgetFrame = Frame(self.MainFrame,bd=18,width=590,height=600, relief=RIDGE, bg = 'cadet blue')
        self.WidgetFrame.grid()


root = Tk()
App = Calculator(root)
root.mainloop()


