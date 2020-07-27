import tkinter
from tkinter import *
from process_module import process
from output_module import output



def send():
    msg = EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)
    if msg != '':
        ChatBox.config(state=NORMAL)
        ChatBox.insert(END, "You: " + msg + '\n\n')
        ChatBox.config(foreground="#446665", font=("Verdana", 12 ))
        res = process(msg)
        ChatBox.insert(END, "Bot: " + res + '\n\n')
        ChatBox.config(state=DISABLED)
        ChatBox.yview(END)
        output(res)


root = Tk()
root.title("Chatbot")
root.geometry("400x500")
root.resizable(width=FALSE, height=FALSE)
ChatBox = Text(root, bd=0, bg="white", height="8", width="50", font="Arial",)
ChatBox.config(state=DISABLED)
scrollbar = Scrollbar(root, command=ChatBox.yview, cursor="heart")
ChatBox['yscrollcommand'] = scrollbar.set
SendButton = Button(root, font=("Verdana",12,'bold'), text="Send", width="12", height=5,
                    bd=0, bg="#f9a602", activebackground="#3c9d9b",fg='#000000',
                    command= send )
EntryBox = Text(root, bd=0, bg="white",width="29", height="5", font="Arial")
scrollbar.place(x=376,y=6, height=386)
ChatBox.place(x=6,y=6, height=386, width=370)
EntryBox.place(x=128, y=401, height=90, width=265)
SendButton.place(x=6, y=401, height=90)
root.mainloop()