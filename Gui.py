from tkinter import * 
import tkinter as tk 
import functions as func #importando arquivo de similaridade
import main as funcMain #para executar algoritmo de similaridade
from tkinter import filedialog
import Kirby as kirby
from tkinter import ttk
from tkinter.font import Font

class Gui:
    folderPy = '' #caminho da pasta com os arquivos .py
    method = '' #peso do método
    parameter = '' #peso parâmetro
    selectionFunction = '' #numero da função de similaridade
    filenameTXT = '' #camingo do arquivo gherkin selectionado

    def criarProjetoTxt(self):
        print("Inserir nome do arquivo (colocar .txt no final)")
        nome = input()
        if len(nome) > 2 and nome.__contains__(".txt"):
            f = open(nome, "w+")
            f.close()

    def abrirProjetoTxt(self):
        print("Selecionar projeto para abrir")
        root = Tk()
        root.filename = filedialog.askopenfilename(initialdir="/",
                                                   title="Select A Project",
                                                   filetypes=(("text files", "*.txt"), ("all files", "*.*")))
        print(root.filename)

    def abrirDiretorio(self):
        root = Tk()
        root.directory = filedialog.askdirectory()
        print(root.directory)

    def __init__(self, master):
        self.master = master
        self.initUI()

        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New Project", command=lambda: self.criarProjetoTxt())
        filemenu.add_command(label="New File", command=self.master.quit)
        filemenu.add_separator()
        filemenu.add_command(label="Open Project", command=lambda: self.abrirProjetoTxt())
        filemenu.add_command(label="Open File", command=lambda: self.abrirDiretorio())
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.master.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        self.master.config(menu=menubar)

    def menuFile(self):
        paths = []
        paths = func.name_file 

        menu = Canvas(self.master, width=300, height=14)
        menu.place(x=995,y=60)

        j = 0
        vFile = tk.IntVar()
        #v.set(1)  # initializing the choice, i.e. Python
        for file in paths:
            tk.Radiobutton(menu, 
            text=file,
            pady=10,
            variable=vFile, 
            value=j).pack(anchor=W)
            j = j + 1

        menuLabelClass = Canvas(self.master, width=3, height=1)
        menuLabelClass.place(x=1400,y=75)

        #label class
        titleClass = Label(menuLabelClass,text="Class :",bg = '#E8E8E8') 
        titleClass["font"] = ("Times New Roman", 10)
        titleClass.pack()

        menuCombo = Canvas(self.master, width=3, height=1)
        menuCombo.place(x=1500,y=75)

        classF = func.name_class
        valuesClass = classF

        #criação combobox
        Vclass = tk.StringVar() 
        comboClass = ttk.Combobox(menuCombo, width = 27, textvariable = Vclass,value=valuesClass)   
        comboClass.grid(column = 1, row = 5) 
        comboClass.current() 

        #Methods
        menuLabelMeth = Canvas(self.master, width=3, height=1)
        menuLabelMeth.place(x=1400,y=110)

        #label methods
        titleMeth = Label(menuLabelMeth,text="Methods :",bg = '#E8E8E8') 
        titleMeth["font"] = ("Times New Roman", 10)
        titleMeth.pack()


        menuCombo2 = Canvas(self.master, width=3, height=1)
        menuCombo2.place(x=1500,y=110)

        MethF = func.lista
        valuesMeth= MethF

        #criação combobox
        Vmeth = tk.StringVar() 
        comboMeth = ttk.Combobox(menuCombo2, width = 27, textvariable = Vmeth,value=valuesMeth)   
        comboMeth.grid(column = 1, row = 5) 
        comboMeth.current() 

       
        #Parameters
        menuLabelPar = Canvas(self.master, width=3, height=1)
        menuLabelPar.place(x=1400,y=145)

        #label parameters
        titlePar = Label(menuLabelPar,text="Parameters :",bg = '#E8E8E8') 
        titlePar["font"] = ("Times New Roman", 10)
        titlePar.pack()

        menuCombo3 = Canvas(self.master, width=3, height=1)
        menuCombo3.place(x=1500,y=145)

        parametersF = func.Finalparameters
        valuesPar = parametersF

        #criação combobox
        Vpar = tk.StringVar() 
        comboPar = ttk.Combobox(menuCombo3, width = 27, textvariable = Vpar,value=valuesPar)   
        comboPar.grid(column = 1, row = 5) 
        comboPar.current() 

        canvasBtn = Canvas(self.master)
        canvasBtn.place(x=1300,y=300)

        btn_OK = Button(canvasBtn,relief=FLAT) 
        btn_OK["text"] = 'OK'
        btn_OK["font"] = ("Verdana", "10")
        btn_OK["bg"] = '#E8E8E8'
        btn_OK["width"] = 5
        btn_OK.pack()
        #btn_OK["command"] = lambda: []

    def FolderTest(self):
        self.directory = filedialog.askdirectory(initialdir=".", title="Select test folder")
        print("folder py: {}".format(self.directory))
        self.folderPy = self.directory

    def SelectTxt(self):
        self.filenameTXT = filedialog.askopenfilename(initialdir=".", title="Select A File", 
        filetypes=(("text files", "*.txt"),("all files", "*.*")))
        print("filename txt: {}".format(self.filenameTXT))
        #kirby.run(open(self.filename,'r'))

    def manipulaString(self,palavra):
        palavra = str(palavra)
        ''.join(palavra)
        palavra = palavra.replace('[(',"")
        palavra = palavra.replace(')])',"")
        caracteres = "(}"
        for i in range(0,len(caracteres)):
            palavra = palavra.replace(caracteres[i],"")
        lis = palavra.split('),')
        listWords = []
        for word in lis: #separar cada item do vetor lis por parenteses
            listWords.append("      (" + word+")")
            #listWords.append( word +"\n")
        meth_par = ''.join(listWords)
        return meth_par
        


    #tabela com as informações dos arquivos Gherkin e os arquivos do usuário
    def set_widgets(self):
        # Inicia o Treeview com as seguintes colunas:
        self.dataCols = ('scenarios','class', 'methods and parameters')
        self.tree = ttk.Treeview(columns=self.dataCols, show='headings',height=14)
        self.tree.column('methods and parameters',width=400)
        self.tree.column('scenarios',width=300)
        self.tree.place(x=985,y=33)
        #style = ttk.Style(self.master) #ajustar altura da linha
        #style.configure("Treeview", rowheight=45)

        # Barra de rolagem
        canvasScrollVertical = Canvas(self.master) 
        canvasScrollVertical.place(x=1783,y=33)
        scrollH = Scrollbar(canvasScrollVertical,width=13)
        scrollH.config(command = self.tree.yview)
        scrollH.grid(ipady=133)
        self.tree.config(yscrollcommand=scrollH.set)

        canvasScrollHorizontal = Canvas(self.master,width=1,height=5)
        canvasScrollHorizontal.place(x=985,y=315)
        scrollV = Scrollbar(canvasScrollHorizontal,orient=tk.HORIZONTAL,width=13)
        scrollV.config(command = self.tree.xview)
        scrollV.grid(ipadx=380)
        self.tree.config(xscrollcommand=scrollV.set)

        # Define o textos do cabeçalho (nome em maiúsculas)
        for c in self.dataCols:
            self.tree.heading(c, text=c.title())

        #pegando caminho dos arquivos
        paths = []
        paths = func.name_file 
        paths.append(self.filenameTXT)
        print("paths: {}".format(paths))
        tamPaths = len(paths)
        #MAP da functions.py
        nameClass = func.name_class
        #filec = func.FileClass()
        #dados = filec.file_class(self.filenameTXT)
        #print("caminho: {}".format(dados.items()))
        filec = func.MethodClass()
        dados = filec.meth_class()

        #self.data = [(paths[0], nameClass[0], self.manipulaString(dados[nameClass[0]]) )]
        self.data=[]
        i = 0
        while(i<tamPaths):
            self.data.append([paths[i], nameClass[i], self.manipulaString(dados[nameClass[i]])])
            i = i + 1


        # Insere cada item dos dados
        for item in self.data:
            self.tree.insert('', 'end', values=item)

        canvasBtn = Canvas(self.master)
        canvasBtn.place(x=1300,y=335)

        btn_edit = Button(canvasBtn,relief=FLAT) 
        btn_edit["text"] = 'Edit'
        btn_edit["font"] = ("Verdana", "10")
        btn_edit["bg"] = '#E8E8E8'
        btn_edit["width"] = 5
        btn_edit.pack()
        #btn_edit.place(x=1300,y=335)
        btn_edit["command"] = lambda: [self.tree.place(x=5000000,y=50000000),
        self.hideCanvas(canvasScrollHorizontal),self.hideCanvas(canvasScrollVertical),self.menuFile(),
        self.hideCanvas(canvasBtn)]

    #comando do botão gerar
    def GenerateTestCode(self):
        if(self.filenameTXT == ''):
            self.filenameTXT = filedialog.askopenfilename(initialdir=".", title="Select File", 
            filetypes=(("text files", "*.txt"),("all files", "*.*")))
            print("filename txt: {}".format(self.filenameTXT))
            if(self.folderPy == ''):
                self.directory = filedialog.askdirectory(initialdir=".", title="Select test folder")
                print("folder py: {}".format(self.directory))
                self.folderPy = self.directory
        if(self.filenameTXT != '' and self.folderPy != '' and self.method == ''):
            kirby.run(open(self.filenameTXT,'r'))
            funcMain.run(-1,-1,-1,self.directory,self.filenameTXT)
            self.set_widgets()
        elif(self.filenameTXT != '' and self.folderPy != '' and self.method != ''):
            kirby.run(open(self.filenameTXT,'r'))
            funcMain.run(self.method,self.parameter,self.selectionFunction,self.directory,self.filenameTXT)
            self.set_widgets()

    #print da escolha das variaveis de peso e da escolha dos algoritmos probabilisticos
    def Select_Ok(self,v):
        if(self.t1.get() != "" and self.t2.get() != ""):
            self.method=float(self.t1.get())  # *0.1 (tranformar)
            self.parameter=float(self.t2.get())

            self.selectionFunction = str(self.v.get())
            print("selection = {}".format(self.selectionFunction))
            print("method = {}".format(self.method))
            print("parameter = {}".format(self.parameter))
        else:
            print("campo vazio")

    def hideCanvas(self,Canvas):
        cv = Canvas
        cv.place(x=30000,y=300000)         #cv.place_forget()

    def showCanvas(self,Canvas):
        cv = Canvas
        cv.place(x=10,y=102)

    #comando do botão 'Scenarios'
    def btnScenario(self):
        menu = Canvas(self.master, width=219, height=725, bg = '#E8E8E8')
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
        btn_test["text"] = 'Test Folder'
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
        menu = Canvas(self.master, width=219, height=725, bg = '#E8E8E8')
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
        btn_scenario["command"] = lambda: [self.btnScenario(),self.hideCanvas(menu),self.SelectTxt()]

        btn_test = Button(menu,relief=FLAT) 
        btn_test["text"] = 'Test Folder'
        btn_test["font"] = font
        btn_test["bg"] = '#E8E8E8'
        btn_test["width"] = 12
        btn_test.place(x=110,y=1)
        btn_test["command"] = lambda: [self.hideCanvas(menu),self.btnScenarioText(),self.FolderTest()]

        btn_opt = Button(menu,relief=FLAT) 
        btn_opt["text"] = 'options'
        btn_opt["font"] = font
        btn_opt["bg"] = '#E8E8E8'
        btn_opt["width"] = 5
        btn_opt.place(x=1,y=700)
        btn_opt["command"] = lambda: [self.options_command(btn_opt,menu)]

    #comando do botão 'Options'
    def btnOptions(self,cv1):
        menu = Canvas(self.master, width=219, height=725, bg = '#E8E8E8')
        menu.place(x=1,y=33)

        #algoritmos WordNet
        title = Label(menu,text="Probabilistic Algorithms",bg = '#E8E8E8') 
        title["font"] = ("Verdana",11)
        title.place(x=2,y=50)

        self.v = IntVar()
        Radiobutton(menu, text="LCH", variable=self.v, value=1,bg='#E8E8E8').place(x=80,y=100,anchor=W)
        Radiobutton(menu, text="WUP", variable=self.v, value=2,bg='#E8E8E8').place(x=80,y=130,anchor=W)
        Radiobutton(menu, text="PATH", variable=self.v, value=3,bg='#E8E8E8').place(x=80,y=160,anchor=W)
        Radiobutton(menu, text="RES", variable=self.v, value=4,bg='#E8E8E8').place(x=80,y=190,anchor=W)
        Radiobutton(menu, text="JCN", variable=self.v, value=5,bg='#E8E8E8').place(x=80,y=220,anchor=W)
        Radiobutton(menu, text="LIN", variable=self.v, value=6,bg='#E8E8E8').place(x=80,y=250,anchor=W)

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
        self.b1=Button(menu, text='OK', command=lambda: self.Select_Ok(self.v))
        self.b1.place(x=90, y=440)

        #buttons canvas
        font=("Verdana", "10")

        btn_scenario = Button(menu,relief=FLAT) 
        btn_scenario["text"] = 'File scenarios'
        btn_scenario["font"] = font
        btn_scenario["bg"] = '#E8E8E8'
        btn_scenario["width"] = 12
        btn_scenario.place(x=1,y=1)
        btn_scenario["command"] = lambda: [self.btnScenario(),self.hideCanvas(menu),self.SelectTxt()]

        btn_test = Button(menu,relief=FLAT) 
        btn_test["text"] = 'Test Folder'
        btn_test["font"] = font
        btn_test["bg"] = '#E8E8E8'
        btn_test["width"] = 12
        btn_test.place(x=110,y=1)
        btn_test["command"] = lambda: [self.btnFileTest(),self.hideCanvas(menu),self.FolderTest()]

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
        menu = Canvas(self.master, width=219, height=725, bg = '#E8E8E8')
        menu.place(x=1,y=33)

        font=("Verdana", "10")

        btn_scenario = Button(menu,relief=FLAT) 
        btn_scenario["text"] = 'File scenarios'
        btn_scenario["font"] = font
        btn_scenario["bg"] = '#E8E8E8'
        btn_scenario["width"] = 12
        btn_scenario.place(x=1,y=1)
        btn_scenario["command"] = lambda: [self.btnScenario(),self.hideCanvas(menu),self.SelectTxt()]

        btn_test = Button(menu,relief=FLAT) 
        btn_test["text"] = 'Test Folder'
        btn_test["font"] = font
        btn_test["bg"] = '#E8E8E8'
        btn_test["width"] = 12
        btn_test.place(x=110,y=1)
        btn_test["command"] = lambda: [self.btnFileTest(),self.hideCanvas(menu),self.FolderTest()]

        btn_opt = Button(menu,relief=FLAT) 
        btn_opt["text"] = 'options'
        btn_opt["font"] = font
        btn_opt["bg"] = '#E8E8E8'
        btn_opt["width"] = 5
        btn_opt.place(x=1,y=700)
        btn_opt["command"] = lambda: [self.options_command(btn_opt,menu)]

        
    def initUI(self):
        self.master.title("BDD Testing")
        self.master.resizable(width=False, height=False) #redimensionar janela
        #self.pack(fill=BOTH, expand=1)

        #title = Label(self,text="BDD Testing") 
        #title["font"] = ("Courier",20,'bold')
        #title.place(x=785,y=15)

        text = Text(self.master, font="arial 12", width=82,height = 40)

        scrollHorizontal = Scrollbar(self.master,width=15)
        scrollHorizontal.config(command = text.yview)
        scrollHorizontal.grid(ipady=345,padx=965,pady=33)
        text.config(yscrollcommand=scrollHorizontal.set)

        text.config(bg="WHITE")
        text.place(x=222,y=33)

        #Scenario Text
        canvas1 = Canvas(self.master, width=980, height=30, bg = '#E8E8E8') 
        canvas1.place(x=1,y=1)
        canvas1.create_text(65,22,font=("Courier","10"),text="Scenarios text")

        #botoes do scenario text
        self.btnScenarioText()
        
        #User Files
        canvas2 = Canvas(self.master, width=815, height=30, bg = '#E8E8E8') 
        canvas2.place(x=980,y=1)
        canvas2.create_text(55,22,font=("Courier","10"),text="User Files")

        userFiles = Canvas(self.master, width=815, height=330, bg = '#E8E8E8') 
        userFiles.place(x=980,y=33)

        #Test Code
        canvas3 = Canvas(self.master, width=815, height=30, bg = '#E8E8E8') 
        canvas3.place(x=980,y=370)
        canvas3.create_text(55,22,font=("Courier","10"),text="Test Code")

        GenerateCode = Canvas(self.master, width=815, height=350, bg = '#E8E8E8') 
        GenerateCode.place(x=980,y=402)

        #Buttons
        bt_Generate = Button(self.master)
        bt_Generate["text"] = "Generate"
        bt_Generate["font"] = ("Verdana", "10")
        bt_Generate["width"] = 12
        bt_Generate.place(x=450,y=780)
        bt_Generate["command"] = lambda:[self.GenerateTestCode()] 

        bt_Results = Button(self.master)
        bt_Results["text"] = "results"
        bt_Results["font"] = ("Verdana", "10")
        bt_Results["width"] = 7
        bt_Results.place(x=1250,y=780)
        #bt_Results["command"] = lambda:[Results(w)]

        bt_close= Button(self.master)
        bt_close["text"] = "close"
        bt_close["font"] = ("Verdana", "10")
        bt_close["width"] = 5
        bt_close.place(x=1350,y=780)
        bt_close["command"] = self.master.quit 

   

def main():
    root = Tk()
    root.geometry('1800x870+800+600')
    Gui(root)
    root.mainloop()  

if __name__ == '__main__':
    main()  
