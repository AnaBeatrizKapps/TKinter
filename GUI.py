from tkinter import * 
import tkinter as tk 
class Gui():
    #Criando a janela...
    window = Tk()
    window.wm_title("NLP")
    window.geometry('1500x850+800+600')
    window.resizable(width=False, height=False) #redimensionar janela

    title = Label(window,text="BDD Testing") 
    title["font"] = ("Courier",20,'bold')
    title.place(x=585,y=15)

    #Scenarios text
    canvas1 = Canvas(window, width=730, height=40, bg = '#E8E8E8') 
    canvas1.place(x=10,y=60)
    canvas1.create_text(90,22,font=("Courier","15"),text="Scenarios text")

    menu = Canvas(window, width=200, height=655, bg = '#E8E8E8')
    menu.place(x=10,y=102)

    text = tk.Text(window, font="arial 12", width=56,height = 36)

    scrollHorizontal = tk.Scrollbar(window,width=15)
    scrollHorizontal.config(command = text.yview)
    scrollHorizontal.grid(ipady=310,padx=725,pady=102)
    text.config(yscrollcommand=scrollHorizontal.set)

    text.config(bg="WHITE")
    text.place(x=213,y=102) 

    #User Files
    canvas2 = Canvas(window, width=730, height=40, bg = '#E8E8E8') 
    canvas2.place(x=760,y=60)
    canvas2.create_text(60,22,font=("Courier","15"),text="User Files")

    userFiles = Canvas(window, width=730, height=300, bg = '#E8E8E8') 
    userFiles.place(x=760,y=102)

    #Generate Test Code
    canvas3 = Canvas(window, width=730, height=40, bg = '#E8E8E8') 
    canvas3.place(x=760,y=415)
    canvas3.create_text(105,22,font=("Courier","15"),text="Generate Test Code")

    GenerateCode = Canvas(window, width=730, height=300, bg = '#E8E8E8') 
    GenerateCode.place(x=760,y=457)

    #Buttons
    bt_Generate = Button(window)
    bt_Generate["text"] = "Generate Test Code"
    bt_Generate["font"] = ("Verdana", "10")
    bt_Generate["width"] = 20
    bt_Generate.place(x=300,y=780)
    #bt_Generate["command"] = lambda:[GenerateTestCode(window)] 

    bt_Results = Button(window)
    bt_Results["text"] = "results"
    bt_Results["font"] = ("Verdana", "10")
    bt_Results["width"] = 7
    bt_Results.place(x=1000,y=780)
    #bt_Results["command"] = lambda:[Results(w)]

    bt_close= Button(window)
    bt_close["text"] = "close"
    bt_close["font"] = ("Verdana", "10")
    bt_close["width"] = 5
    bt_close.place(x=1100,y=780)
    bt_close["command"] = window.quit

    def run(self):
        Gui.window.mainloop()