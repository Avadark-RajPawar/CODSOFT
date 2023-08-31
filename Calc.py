import tkinter as tk

Light_Gray = '#f5f5f5'
White = '#FFFFFF'
Label_Color = '#25265E'
OffWhite = '#F8FAFF'
Light_Blue = '#CCEDFF'

Small = ('Arial', 16)
Large = ('Arial', 40, "bold")
Digits = ('Arial', 24, 'bold')
Operator = ('Arial', 20)


class Calculator:
    def __init__(self, window):
        self.window = window
        self.window.geometry("375x667+600+50")
        self.window.title("Calculator")
        self.window.resizable(False, False)

        self.Icon = tk.PhotoImage(file="Images/Calc.png")
        self.window.iconphoto(False, self.Icon)

        self.total = ""
        self.current = ""

        self.Display_frame = self.Create_Displayframe()
        self.total_label, self.label = self.Create_Displaylabels()

        self.Buttons = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3,),
            0: (4, 1), '.': (4, 2)
        }
        self.Opertaors = {
            "/": "\u00f7", "*": "\u00d7", "-": "-", "+": "+"
        }
        self.Button_frame = self.Create_Buttonframe()

        self.Button_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.Button_frame.rowconfigure(x, weight=1)
            self.Button_frame.columnconfigure(x, weight=1)
        self.Create_Buttons()
        self.Create_Operators()
        self.Create_Clearbutton()
        self.Create_Sqrbutton()
        self.Create_Equalbutton()
        self.Create_Sqrootbutton()


    def run(self):
        self.window.mainloop()

    def add_label(self, value):
        self.current += str(value)
        self.Update_Label()

    def add_operator(self, value):
        self.current += str(value)
        self.total += self.current
        self.current = ""
        self.Update_Label()
        self.Update_Total()

    def sqr(self):
        self.current = str(eval(f"{self.current}**2"))
        self.Update_Label()

    def sqroot(self):
        self.current = str(eval(f"{self.current}**0.5"))
        self.Update_Label()

    def clear_all(self):
        self.current = ""
        self.total = ""
        self.Update_Total()
        self.Update_Label()

    def evaluate(self):
        self.total += self.current
        self.Update_Total()
        self.current = str(eval(self.total))
        self.total = ""
        self.Update_Label()
    def Create_Displayframe(self):
        frame = tk.Frame(self.window, height=221, bg=Light_Gray)
        frame.pack(expand=True, fill='both')
        return frame

    def Create_Buttonframe(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill='both')
        return frame

    def Create_Displaylabels(self):
        total_label = tk.Label(self.Display_frame, text=self.total, anchor=tk.E, bg=Light_Gray, fg=Label_Color, padx=24,
                               font=Small)
        total_label.pack(expand=True, fill='both')

        label = tk.Label(self.Display_frame, text=self.current, anchor=tk.E, bg=Light_Gray, fg=Label_Color, padx=24,
                         font=Large)
        label.pack(expand=True, fill='both')

        return total_label, label

    def Create_Buttons(self):
        for digit, grid in self.Buttons.items():
            button = tk.Button(self.Button_frame, text=str(digit), bg=White, fg=Label_Color, font=Digits, borderwidth=0, command=lambda x=digit: self.add_label(x))
            button.grid(row=grid[0], column=grid[1], sticky=tk.NSEW)

    def Create_Operators(self):
        i = 0
        for operation, sym in self.Opertaors.items():
            button = tk.Button(self.Button_frame, text=str(operation), bg=OffWhite, fg=Label_Color, font=Operator,
                              borderwidth=0, command=lambda x=operation : self.add_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)

            i += 1

    def Create_Clearbutton(self):
        button = tk.Button(self.Button_frame, text="C", bg=OffWhite, fg=Label_Color, font=Operator, borderwidth=0, command=lambda: self.clear_all())
        button.grid(row=0, column=1, sticky=tk.NSEW)

    def Create_Sqrbutton(self):
        button = tk.Button(self.Button_frame, text="x\u00b2", bg=OffWhite, fg=Label_Color, font=Operator, borderwidth=0, command=lambda: self.sqr())
        button.grid(row=0, column=2, sticky=tk.NSEW)

    def Create_Sqrootbutton(self):
        button = tk.Button(self.Button_frame, text="\u221ax", bg=OffWhite, fg=Label_Color, font=Operator, borderwidth=0, command=lambda: self.sqroot())
        button.grid(row=0, column=3, sticky=tk.NSEW)

    def Create_Equalbutton(self):
        button = tk.Button(self.Button_frame, text="=", bg=Light_Blue, fg=Label_Color, font=Operator, borderwidth=0, command=lambda : self.evaluate())
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

    def Update_Total(self):
        self.total_label.config(text=self.total)

    def Update_Label(self):
        self.label.config(text=self.current[:11])

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    calculator.run()


