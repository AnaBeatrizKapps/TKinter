from tkinter import * 
import tkinter as tk 

class Gui(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.parent = parent
        self.initUI()

        menubar = Menu(parent)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New Project", command=parent.quit)
        filemenu.add_command(label="New File", command=parent.quit)
        filemenu.add_separator()
        filemenu.add_command(label="Open Project", command=parent.quit)
        filemenu.add_command(label="Open File", command=parent.quit)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=parent.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        parent.config(menu=menubar)

    #print da escolha das variaveis de peso e da escolha dos algoritmos probabilisticos
    def Select_Ok(self,v):
        num1=float(self.t1.get())  # *0.1 (tranformar)
        num2=float(self.t2.get()) 
        print("method = {}".format(num1))
        print("parameter = {}".format(num2))
        selection = "You selected the option " + str(v.get())
        print(selection)

    def hideCanvas(self,Canvas):
        cv = Canvas
        cv.place(x=30000,y=300000)         #cv.place_forget()

    def showCanvas(self,Canvas):
        cv = Canvas
        cv.place(x=10,y=102)

    #comando do botão 'Scenarios'
    def btnScenario(self):
        menu = Canvas(self, width=219, height=725, bg = '#E8E8E8')
        menu.place(x=1,y=33)

        title = Label(menu,text="Comando Scenario",bg = '#E8E8E8') 
        title["font"] = ("Verdana",11)
        title.place(x=2,y=50)

        font=("Verdana", "10")

        btn_scenario = Button(menu,relief=FLAT) 
        btn_scenario["text"] = 'File scenarios'
        btn_scenario["font"] = font
        btn_scenario["bg"] = '#E8E8E8'
        btn_scenario["width"] = 12
        btn_scenario.place(x=1,y=1)
        btn_scenario["command"] = lambda: [self.hideCanvas(menu),self.btnScenarioText()]

        btn_test = Button(menu,relief=FLAT) 
        btn_test["text"] = 'File test'
        btn_test["font"] = font
        btn_test["bg"] = '#E8E8E8'
        btn_test["width"] = 12
        btn_test.place(x=110,y=1)
        btn_test["command"] = lambda: [self.btnFileTest(),self.hideCanvas(menu)]

        btn_opt = Button(menu,relief=FLAT) 
        btn_opt["text"] = 'options'
        btn_opt["font"] = font
        btn_opt["bg"] = '#E8E8E8'
        btn_opt["width"] = 5
        btn_opt.place(x=1,y=700)
        btn_opt["command"] = lambda: [self.options_command(btn_opt,menu)]

    #comando do botão 'File test'
    def btnFileTest(self):
        menu = Canvas(self, width=219, height=725, bg = '#E8E8E8')
        menu.place(x=1,y=33)

        title = Label(menu,text="Comando File Text",bg = '#E8E8E8') 
        title["font"] = ("Verdana",11)
        title.place(x=2,y=50)

        font=("Verdana", "10")

        btn_scenario = Button(menu,relief=FLAT) 
        btn_scenario["text"] = 'File scenarios'
        btn_scenario["font"] = font
        btn_scenario["bg"] = '#E8E8E8'
        btn_scenario["width"] = 12
        btn_scenario.place(x=1,y=1)
        btn_scenario["command"] = lambda: [self.btnScenario(),self.hideCanvas(menu)]

        btn_test = Button(menu,relief=FLAT) 
        btn_test["text"] = 'File test'
        btn_test["font"] = font
        btn_test["bg"] = '#E8E8E8'
        btn_test["width"] = 12
        btn_test.place(x=110,y=1)
        btn_test["command"] = lambda: [self.hideCanvas(menu),self.btnScenarioText()]

        btn_opt = Button(menu,relief=FLAT) 
        btn_opt["text"] = 'options'
        btn_opt["font"] = font
        btn_opt["bg"] = '#E8E8E8'
        btn_opt["width"] = 5
        btn_opt.place(x=1,y=700)
        btn_opt["command"] = lambda: [self.options_command(btn_opt,menu)]

    #comando do botão 'Options'
    def btnOptions(self,cv1):
        menu = Canvas(self, width=219, height=725, bg = '#E8E8E8')
        menu.place(x=1,y=33)

        #algoritmos WordNet
        title = Label(menu,text="Probabilistic Algorithms",bg = '#E8E8E8') 
        title["font"] = ("Verdana",11)
        title.place(x=2,y=50)

        v = IntVar()
        Radiobutton(menu, text="HSO", variable=v, value=1,bg='#E8E8E8').place(x=90,y=100,anchor=W)
        Radiobutton(menu, text="LCH", variable=v, value=2,bg='#E8E8E8').place(x=90,y=130,anchor=W)
        Radiobutton(menu, text="LESK", variable=v, value=3,bg='#E8E8E8').place(x=90,y=160,anchor=W)
        Radiobutton(menu, text="WUP", variable=v, value=4,bg='#E8E8E8').place(x=90,y=190,anchor=W)
        Radiobutton(menu, text="RES", variable=v, value=5,bg='#E8E8E8').place(x=90,y=220,anchor=W)
        Radiobutton(menu, text="PATH", variable=v, value=6,bg='#E8E8E8').place(x=90,y=250,anchor=W)
        Radiobutton(menu, text="JCN", variable=v, value=7,bg='#E8E8E8').place(x=90,y=280,anchor=W)
        Radiobutton(menu, text="LIN", variable=v, value=8,bg='#E8E8E8').place(x=90,y=310,anchor=W)

        #pesos
        titleW = Label(menu,text="weights:",bg = '#E8E8E8') 
        titleW["font"] = ("Verdana",11)
        titleW.place(x=15,y=350)

        self.lbl1=Label(menu, text='method',bg='#E8E8E8',font = ("Verdana",11))
        self.t1=Entry(menu,bd=1,width=10)
        self.lbl1.place(x=15, y=380)
        self.t1.place(x=100, y=380)

        self.lbl2=Label(menu, text='parameter',bg='#E8E8E8',font = ("Verdana",11))
        self.t2=Entry(menu,bd=1,width=10)
        self.lbl2.place(x=15, y=400)
        self.t2.place(x=100, y=400)

        self.btn1 = Button(menu, text='OK')
        self.b1=Button(menu, text='OK', command=lambda: self.Select_Ok(v))
        self.b1.place(x=90, y=440)

        #buttons canvas
        font=("Verdana", "10")

        btn_scenario = Button(menu,relief=FLAT) 
        btn_scenario["text"] = 'File scenarios'
        btn_scenario["font"] = font
        btn_scenario["bg"] = '#E8E8E8'
        btn_scenario["width"] = 12
        btn_scenario.place(x=1,y=1)
        btn_scenario["command"] = lambda: [self.btnScenario(),self.hideCanvas(menu)]

        btn_test = Button(menu,relief=FLAT) 
        btn_test["text"] = 'File test'
        btn_test["font"] = font
        btn_test["bg"] = '#E8E8E8'
        btn_test["width"] = 12
        btn_test.place(x=110,y=1)
        btn_test["command"] = lambda: [self.btnFileTest(),self.hideCanvas(menu)]

        btn_opt = Button(menu,relief=FLAT) 
        btn_opt["text"] = 'options'
        btn_opt["font"] = font
        btn_opt["bg"] = '#E8E8E8'
        btn_opt["width"] = 5
        btn_opt.place(x=1,y=700)
        btn_opt["command"] = lambda: [self.hideCanvas(menu),self.btnScenarioText()]

    #comando do botão 'Options'
    def options_command(self,Button_opt,Canvas):
        cv1 = Canvas
        self.hideCanvas(cv1)
        self.btnOptions(cv1)

    #botoes Scenarios text 
    def btnScenarioText(self):
        menu = Canvas(self, width=219, height=725, bg = '#E8E8E8')
        menu.place(x=1,y=33)

        font=("Verdana", "10")

        btn_scenario = Button(menu,relief=FLAT) 
        btn_scenario["text"] = 'File scenarios'
        btn_scenario["font"] = font
        btn_scenario["bg"] = '#E8E8E8'
        btn_scenario["width"] = 12
        btn_scenario.place(x=1,y=1)
        btn_scenario["command"] = lambda: [self.btnScenario(),self.hideCanvas(menu)]

        btn_test = Button(menu,relief=FLAT) 
        btn_test["text"] = 'File test'
        btn_test["font"] = font
        btn_test["bg"] = '#E8E8E8'
        btn_test["width"] = 12
        btn_test.place(x=110,y=1)
        btn_test["command"] = lambda: [self.btnFileTest(),self.hideCanvas(menu)]

        btn_opt = Button(menu,relief=FLAT) 
        btn_opt["text"] = 'options'
        btn_opt["font"] = font
        btn_opt["bg"] = '#E8E8E8'
        btn_opt["width"] = 5
        btn_opt.place(x=1,y=700)
        btn_opt["command"] = lambda: [self.options_command(btn_opt,menu)]

        
    def initUI(self):
        self.parent.title("BDD Testing")
        self.parent.resizable(width=False, height=False) #redimensionar janela
        self.pack(fill=BOTH, expand=1)

        #title = Label(self,text="BDD Testing") 
        #title["font"] = ("Courier",20,'bold')
        #title.place(x=785,y=15)

        text = tk.Text(self, font="arial 12", width=82,height = 40)

        scrollHorizontal = tk.Scrollbar(self,width=15)
        scrollHorizontal.config(command = text.yview)
        scrollHorizontal.grid(ipady=345,padx=965,pady=33)
        text.config(yscrollcommand=scrollHorizontal.set)

        text.config(bg="WHITE")
        text.place(x=222,y=33)

        #Scenario Text
        canvas1 = Canvas(self, width=980, height=30, bg = '#E8E8E8') 
        canvas1.place(x=1,y=1)
        canvas1.create_text(65,22,font=("Courier","10"),text="Scenarios text")

        #botoes do scenario text
        self.btnScenarioText()
        
        #User Files
        canvas2 = Canvas(self, width=815, height=30, bg = '#E8E8E8') 
        canvas2.place(x=980,y=1)
        canvas2.create_text(55,22,font=("Courier","10"),text="User Files")

        userFiles = Canvas(self, width=815, height=330, bg = '#E8E8E8') 
        userFiles.place(x=980,y=33)

        #Test Code
        canvas3 = Canvas(self, width=815, height=30, bg = '#E8E8E8') 
        canvas3.place(x=980,y=370)
        canvas3.create_text(55,22,font=("Courier","10"),text="Test Code")

        GenerateCode = Canvas(self, width=815, height=350, bg = '#E8E8E8') 
        GenerateCode.place(x=980,y=402)

        #Buttons
        bt_Generate = Button(self)
        bt_Generate["text"] = "Generate"
        bt_Generate["font"] = ("Verdana", "10")
        bt_Generate["width"] = 12
        bt_Generate.place(x=450,y=780)
        #bt_Generate["command"] = lambda:[GenerateTestCode(window)] 

        bt_Results = Button(self)
        bt_Results["text"] = "results"
        bt_Results["font"] = ("Verdana", "10")
        bt_Results["width"] = 7
        bt_Results.place(x=1250,y=780)
        #bt_Results["command"] = lambda:[Results(w)]

        bt_close= Button(self)
        bt_close["text"] = "close"
        bt_close["font"] = ("Verdana", "10")
        bt_close["width"] = 5
        bt_close.place(x=1350,y=780)
        bt_close["command"] = self.quit 

        

        

def main():
    root = Tk()
    root.geometry('1800x870+800+600')
    app = Gui(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  