from tkinter import *

result = None

def messageWindow(message):
    win = Toplevel()

    frame = Frame(win)
    frame.place(anchor="c", relx=.5, rely=.5)
    
    Label(frame, text=message).pack()
    
    Button(frame, text='Promote', command=lambda:[win.destroy(), returnValue(True)]).pack()
    Button(frame, text='Do not promote', command=lambda:[win.destroy(), returnValue(False)]).pack()

    win.wait_window()
                                                       
    return result

def returnValue(value):
    global result
    result = value


def multiOptionWindow(message, *args):
    win = Toplevel()

    frame = Frame(win)
    frame.place(anchor="c", relx=.5, rely=.5)
    
    Label(frame, text=message).pack()

    for arg in args:
        
        Button(frame, text=arg, command=lambda a=arg: (returnValue(a),
                                                     win.destroy())).pack()
        
    win.wait_window()
                                                       
    return result




def popupWindow(root, message):
    popup_menu = Menu(root, tearoff = 0)
    popup_menu.add_command(label = message, command=lambda: returnValue(1))
    popup_menu.add_command(label = "Do not promote", command=lambda: returnValue(0))

    popup_menu.tk_popup(root.winfo_pointerx(), root.winfo_pointery())
    
    return result




