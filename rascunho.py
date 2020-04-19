from tkinter import * 
import tkinter as tk 

class Gui(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.parent = parent
        self.initUI()

    #func1: função para esconder objeto Entry 
    def hideEntry(self,Entry1,Entry2):
        Entry1.place_forget()
        Entry2.place_forget()

    #print das variaveis dos pesos
    def Select_Ok(self,v):
        num1=float(self.t1.get())  # *0.1 (tranformar)
        num2=float(self.t2.get()) 
        print("method = {}".format(num1))
        print("parameter = {}".format(num2))
        selection = "You selected the option " + str(v.get())
        print(selection)

    #Opções: selecionar função de probabilidade e digitar peso
    def FileTest_Selection(self):
        #algoritmos WordNet
        title = Label(self,text="Probabilistic Algorithms",bg = '#E8E8E8') 
        title["font"] = ("Verdana",11)
        title.place(x=10,y=130)

        v = IntVar()
        Radiobutton(self, text="HSO", variable=v, value=1,bg='#E8E8E8').place(x=90,y=160,anchor=W)
        Radiobutton(self, text="LCH", variable=v, value=2,bg='#E8E8E8').place(x=90,y=190,anchor=W)
        Radiobutton(self, text="LESK", variable=v, value=3,bg='#E8E8E8').place(x=90,y=220,anchor=W)
        Radiobutton(self, text="WUP", variable=v, value=4,bg='#E8E8E8').place(x=90,y=250,anchor=W)
        Radiobutton(self, text="RES", variable=v, value=5,bg='#E8E8E8').place(x=90,y=280,anchor=W)
        Radiobutton(self, text="PATH", variable=v, value=6,bg='#E8E8E8').place(x=90,y=310,anchor=W)
        Radiobutton(self, text="JCN", variable=v, value=7,bg='#E8E8E8').place(x=90,y=340,anchor=W)
        Radiobutton(self, text="LIN", variable=v, value=8,bg='#E8E8E8').place(x=90,y=370,anchor=W)

        #pesos
        titleW = Label(self,text="weights:",bg = '#E8E8E8') 
        titleW["font"] = ("Verdana",11)
        titleW.place(x=15,y=420)

        self.lbl1=Label(self, text='method',bg='#E8E8E8',font = ("Verdana",11))
        self.t1=Entry(bd=1,width=10)
        self.lbl1.place(x=15, y=450)
        self.t1.place(x=100, y=450)

        self.lbl2=Label(self, text='parameter',bg='#E8E8E8',font = ("Verdana",11))
        self.t2=Entry(bd=1,width=10)
        self.lbl2.place(x=15, y=475)
        self.t2.place(x=100, y=475)

        self.btn1 = Button(self, text='OK')
        self.b1=Button(self, text='OK', command=lambda: self.Select_Ok(v))
        self.b1.place(x=90, y=520)

    #comando do botão 'File'
    def file_command(self,Button_fl,Button_sc,Button_ts,Button_opt):
        btn_fl = Button_fl
        btn_fl.config(bg="#A9A9A9")
        btn_fl["command"] = lambda: self.initUI()
        #btn_fl["command"] = lambda: btn_fl.config(bg="#E8E8E8")

        btn_sc = Button_sc
        btn_sc.config(bg="#E8E8E8")
        btn_sc["command"] = lambda: self.scenario_command(Button_fl,Button_sc,Button_ts,Button_opt)

        btn_ts = Button_ts
        btn_ts.config(bg="#E8E8E8")
        btn_ts["command"] = lambda: self.test_command(Button_fl,Button_sc,Button_ts,Button_opt)

        btn_opt = Button_opt
        btn_opt.config(bg="#E8E8E8")
        btn_opt["command"] = lambda: [self.options_command(Button_fl,Button_sc,Button_ts,Button_opt),self.FileTest_Selection()]

    #comando do botão 'Scenario'
    def scenario_command(self,Button_fl,Button_sc,Button_ts,Button_opt):
        btn_sc = Button_sc
        btn_sc.config(bg="#A9A9A9")
        btn_sc["command"] = lambda: self.initUI()

        btn_fl = Button_fl
        btn_fl.config(bg="#E8E8E8")
        btn_fl["command"] = lambda: self.file_command(Button_fl,Button_sc,Button_ts,Button_opt)

        btn_ts = Button_ts
        btn_ts.config(bg="#E8E8E8")
        btn_ts["command"] = lambda: self.test_command(Button_fl,Button_sc,Button_ts,Button_opt)

        btn_opt = Button_opt
        btn_opt.config(bg="#E8E8E8")
        btn_opt["command"] = lambda: [self.options_command(Button_fl,Button_sc,Button_ts,Button_opt),self.FileTest_Selection()]

    #comando do botão 'File test'
    def test_command(self,Button_fl,Button_sc,Button_ts,Button_opt):
        btn_ts = Button_ts
        btn_ts.config(bg="#A9A9A9")
        btn_ts["command"] = lambda: self.initUI()

        btn_fl = Button_fl
        btn_fl.config(bg="#E8E8E8")
        btn_fl["command"] = lambda: self.file_command(Button_fl,Button_sc,Button_ts,Button_opt)

        btn_sc = Button_sc
        btn_sc.config(bg="#E8E8E8")
        btn_sc["command"] = lambda: self.scenario_command(Button_fl,Button_sc,Button_ts,Button_opt)

        btn_opt = Button_opt
        btn_opt.config(bg="#E8E8E8")
        btn_opt["command"] = lambda: [self.options_command(Button_fl,Button_sc,Button_ts,Button_opt)]

    #comando do botão 'Options'
    def options_command(self,Button_fl,Button_sc,Button_ts,Button_opt):
        self.FileTest_Selection()
        btn_opt = Button_opt
        btn_opt.config(bg="#A9A9A9")
        btn_opt["command"] = lambda: [self.initUI(),self.hideEntry(self.t1,self.t2)]

        btn_fl = Button_fl
        btn_fl.config(bg="#E8E8E8")
        btn_fl["command"] = lambda: self.file_command(Button_fl,Button_sc,Button_ts,Button_opt)

        btn_sc = Button_sc
        btn_sc.config(bg="#E8E8E8")
        btn_sc["command"] = lambda: self.scenario_command(Button_fl,Button_sc,Button_ts,Button_opt)

        btn_ts = Button_ts
        btn_ts.config(bg="#E8E8E8")
        btn_ts["command"] = lambda: self.test_command(Button_fl,Button_sc,Button_ts,Button_opt)
        
    def initUI(self):
        self.parent.title("NLP")
        self.parent.resizable(width=False, height=False) #redimensionar janela
        self.pack(fill=BOTH, expand=1)

        title = Label(self,text="BDD Testing") 
        title["font"] = ("Courier",20,'bold')
        title.place(x=785,y=15)

        #Scenarios text
        canvas1 = Canvas(self, width=980, height=40, bg = '#E8E8E8') 
        canvas1.place(x=10,y=60)
        canvas1.create_text(90,22,font=("Courier","15"),text="Scenarios text")

        menu = Canvas(self, width=219, height=725, bg = '#E8E8E8')
        menu.place(x=10,y=102)

        text = tk.Text(self, font="arial 12", width=81,height = 40)

        scrollHorizontal = tk.Scrollbar(self,width=15)
        scrollHorizontal.config(command = text.yview)
        scrollHorizontal.grid(ipady=345,padx=972,pady=102)
        text.config(yscrollcommand=scrollHorizontal.set)

        text.config(bg="WHITE")
        text.place(x=235,y=102)

        #User Files
        canvas2 = Canvas(self, width=780, height=40, bg = '#E8E8E8') 
        canvas2.place(x=1000,y=60)
        canvas2.create_text(60,22,font=("Courier","15"),text="User Files")

        userFiles = Canvas(self, width=780, height=330, bg = '#E8E8E8') 
        userFiles.place(x=1000,y=102)

        #Test Code
        canvas3 = Canvas(self, width=780, height=33, bg = '#E8E8E8') 
        canvas3.place(x=1000,y=440)
        canvas3.create_text(60,22,font=("Courier","15"),text="Test Code")

        GenerateCode = Canvas(self, width=780, height=350, bg = '#E8E8E8') 
        GenerateCode.place(x=1000,y=475)

        #Buttons
        bt_Generate = Button(self)
        bt_Generate["text"] = "Generate"
        bt_Generate["font"] = ("Verdana", "10")
        bt_Generate["width"] = 10
        bt_Generate.place(x=450,y=850)
        #bt_Generate["command"] = lambda:[GenerateTestCode(window)] 

        bt_Results = Button(self)
        bt_Results["text"] = "results"
        bt_Results["font"] = ("Verdana", "10")
        bt_Results["width"] = 7
        bt_Results.place(x=1250,y=850)
        #bt_Results["command"] = lambda:[Results(w)]

        bt_close= Button(self)
        bt_close["text"] = "close"
        bt_close["font"] = ("Verdana", "10")
        bt_close["width"] = 5
        bt_close.place(x=1350,y=850)
        bt_close["command"] = self.quit 

        font=("Verdana", "10")
        btn_file = Button(self,relief=FLAT) 
        btn_file["text"] = 'File'
        btn_file["font"] = font
        btn_file["bg"] = '#E8E8E8'
        btn_file["width"] = 5
        btn_file.place(x=11,y=100)
        btn_file["command"] = lambda: [self.file_command(btn_file,btn_scenario,btn_test,btn_opt)]

        btn_scenario = Button(self,relief=FLAT) 
        btn_scenario["text"] = 'Scenarios'
        btn_scenario["font"] = font
        btn_scenario["bg"] = '#E8E8E8'
        btn_scenario["width"] = 8
        btn_scenario.place(x=69,y=100)
        btn_scenario["command"] = lambda: [self.scenario_command(btn_file,btn_scenario,btn_test,btn_opt)]

        btn_test = Button(self,relief=FLAT) 
        btn_test["text"] = 'File Test'
        btn_test["font"] = font
        btn_test["bg"] = '#E8E8E8'
        btn_test["width"] = 8
        btn_test.place(x=145,y=100)
        btn_test["command"] = lambda: [self.test_command(btn_file,btn_scenario,btn_test,btn_opt)]

        btn_opt = Button(self,relief=FLAT) 
        btn_opt["text"] = 'options'
        btn_opt["font"] = font
        btn_opt["bg"] = '#E8E8E8'
        btn_opt["width"] = 5
        btn_opt.place(x=11,y=800)
        btn_opt["command"] = lambda: [self.options_command(btn_file,btn_scenario,btn_test,btn_opt)]


def main():
    root = Tk()
    root.geometry('1800x970+800+600')
    app = Gui(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  