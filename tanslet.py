from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Translator")
root.geometry("500x500")
root.config(bg='skyblue')

lab_txt=Label(root,text="Jarvis",font=("Time New Roman",20,"bold"),bg="skyblue")
lab_txt.place(x=100,y=40,height=50,width=300)

frame = Frame(root).pack(side=BOTTOM)

lab_txt=Label(root,text="Source Text",font=("Time New Roman",20,"bold"),bg="skyblue")
lab_txt.place(x=100,y=80,height=50,width=300)

Sor_txt = Text(frame,font=("Time New Roman",20,"bold"),wrap=WORD)
Sor_txt.place(x=10,y=120,height=100,width=300)

list_text = [1,2,3,4]

comb_sor = ttk.Combobox(frame,value=list_text) 
comb_sor.place(x=10,y=180,height=20,width=40)



root.mainloop()

