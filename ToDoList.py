from tkinter import *
from tkinter import messagebox


def newtask():
    task = task_entry.get()
    if task != "":
        List_frame.insert(END, task)
        task_entry.delete(0, "end")
    else:
        messagebox.showwarning("Warning", "Enter Your Task")


def deletetask():
    List_frame.delete(ANCHOR)


def updatetask():
    old_task = List_frame.get(ANCHOR)
    # task_entry.setvar(old_task)
    new_task = task_entry.get()
    if new_task != "":
        List_frame.delete(ANCHOR)
        List_frame.insert(ANCHOR, new_task)
        task_entry.delete(0, "end")
    else:
        messagebox.showwarning("Warning", "Update your task")


window = Tk()
window.geometry('1000x600+500+200')
window.title('ToDo List')
window.config()
window.resizable(width=False, height=False)

Icon = PhotoImage(file="Images/task (1).png")
window.iconphoto(False, Icon)

# Bg_top = PhotoImage(file="Images/topbar.png")
# Label(window, image=Bg_top).pack(fill=BOTH)

Top_frame = Frame(window, bg='#37B61D', width=1000, height=120)
Top_frame.pack(pady=10)

Heading = Label(window, text="TODO LIST", font="ariel 30 bold", bg='#37B61D')
Heading.place(x=50, y=40)

Entry_frame = Frame(window)
Entry_frame.pack(padx=0, fill=BOTH)

Entry_label = Label(Entry_frame, text='Add Items', font=('Times', 28))
Entry_label.pack(side=TOP)

Child_frame = Frame(Entry_frame)
Child_frame.pack(side=BOTTOM, fill=X)

task_entry = Entry(Child_frame, font=('Times', 24), width=50)
task_entry.pack(side=LEFT, pady=0, fill=BOTH, padx=10)

Add_button = Button(Child_frame, text='ADD', font=('Times', 14), fg='white', bg='black', padx=20, pady=10,
                    command=newtask)
Add_button.pack(side=RIGHT, fill=BOTH, expand=True, padx=10)

frame = Frame(window)
frame.pack(pady=20, fill=BOTH, padx=10)

List_frame = Listbox(frame, width=80, height=8, font=('Times', 18), bd=0, fg='#464646', highlightthickness=0,
                     selectbackground='#a6a6a6', activestyle='none')
List_frame.pack(side=LEFT, fill=BOTH)

Task_list = [
    'Waking Up',
    'Drinking Coffee',
    'Taking Bath',
    'Getting Ready For College'
]

for item in Task_list:
    List_frame.insert(END, item)

Sb_y = Scrollbar(frame)
Sb_y.pack(side=RIGHT, fill=BOTH) \
 \
# Sb_x = Scrollbar(frame)
# Sb_x.pack(side=BOTTOM, fill=BOTH)

List_frame.config(yscrollcommand=Sb_y.set)
Sb_y.config(command=List_frame.yview)
# Sb_x.config(command=List_frame.xview)

Button_frame = Frame(window)
Button_frame.pack(pady=20)

Del_button = Button(Button_frame, text='DELETE', font=('Times', 14), fg='white', bg='#DC2727', padx=20, pady=10,
                    command=deletetask)
Del_button.pack(side=LEFT, fill=BOTH, expand=True)

Up_button = Button(Button_frame, text='UPDATE', font=('Times', 14), fg='white', bg='#1CBADD', padx=20, pady=10,
                   command=updatetask)
Up_button.pack(side=RIGHT, fill=BOTH, expand=True, padx=10)

window.mainloop()
