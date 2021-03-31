from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import showinfo,askquestion
import os

def newfile():
    global file
    root.title("Untiltled - NotePad")
    file=None
    entry.delete(1.0,END)
def openfile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All types","*.*"),("Text Documents","*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+" - Notepad")
        entry.delete(1.0,END)
        f=open(file,'r')
        entry.insert(1.0,f.read())
        f.close()
def save():
    global file
    if file==None:
        file = asksaveasfilename(initialfile='untitled.txt', defaultextension=".txt",filetypes=[("All types", "*.*"), ("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            #save as a new file
            f=open(file, "w")
            f.write(entry.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + " - Notepad")
            print("file saved")
    else:
        #save the file
        f=open(file, "w")
        f.write(entry.get(1.0, END))
        f.close()
def exit():
    var=askquestion('Experience','Do you like this notepad ?')
    if var=="yes":
        showinfo("Rating",'please rate this software')
    root.destroy()
def cut():
    entry.event_generate("<<Cut>>")
def copy():
    entry.event_generate("<<Copy>>")
def paste():
    entry.event_generate("<<Paste>>")
def about():
    showinfo("About", 'This is a notepad created by rajesh yadav on 21/12/2020')

root=Tk()
root.title("Notepad By Rajesh")
root.geometry("600x600")
#add menubar
menubar=Menu(root,)
m1=Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=m1)
m1.add_command(label="New",command=newfile)
m1.add_command(label="open",command=openfile)
m1.add_command(label="save",command=save)
m1.add_separator()
m1.add_command(label="exit",command=exit)

m2=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit",menu=m2)
m2.add_command(label="cut",command=cut)
m2.add_command(label="copy",command=copy)
m2.add_command(label="paste",command=paste)

m3=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=m3)
m3.add_command(label="About",command=about)

root.config(menu=menubar)

#text area
entry=Text(root,font="lucida 15")
file=None
entry.pack(fill=BOTH,expand=True)

#scollbar
scroll=Scrollbar(entry)
scroll.pack(side=RIGHT,fill=Y)
scroll.config(command=entry.yview)
entry.config(yscrollcommand=scroll.set)
root.mainloop()
