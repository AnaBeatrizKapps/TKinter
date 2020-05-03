import os
import importlib
import importlib.util
import inspect 
import nltk
import Kirby as nlp 
import similarity as lch
import similarity as wup
import similarity as path
import similarity as res
import similarity as jcn
import similarity as lin
name_file = [] #lista dos nomes do arquivo do diretorio da pasta cod
Rfile = [] #lista de referencia do diretorio da pasta cod
object_class = [] #lista de objetos das classes
name_class = [] #lista nome das classes
vet_ref = nlp.vetorReferenciaMetodoClasse #vetor referencia a classe
vet_meth = nlp.vetorMetodo  #vetor de metodos
vet_class = nlp.vetorClasse  #vetor de classes
listWord = [] #lista de metodos
listParameter = [] #lista de parametros
lista = [] #lista nome dos métodos das classes da pasta cod
list_Object = [] #lista objeto métodos das classes da pasta cod
listFinalMeth = [] #lista com todos os métodos juntos
parameters = []
map_dados = {} #map(diretorio,classes,metodos,parametros)
Finalparameters = [] #lista com todos os parâmetros separados em grupo

#CAMINHO = ('/home/ana/pasta/cod/') 
class FuncWordNet:
    def SelectFunction(self,selection,word1,word2):
        #print("Selection: {}".format(selection))
        switcher={
                1:lch.similarityLCH(word1,word2),
                2:wup.similarityWUP(word1,word2),
                3:path.similarityPATH(word1,word2),
                4:res.similarityRES(word1,word2),
                5:jcn.similarityJCN(word1,word2),
                6:lin.similarityLIN(word1,word2)
                }
        func=switcher.get(selection,wup.similarityWUP(word1,word2))
        return func

class file_Route:
    def get_file(self,PathFolder): #PathFolder: caminho da pasta
        file = []
        paths_file = os.listdir(PathFolder)
        for path_file in paths_file:
            if str(path_file).endswith('.pyc') or str(path_file).endswith('checkpoints') or str(path_file).endswith('__'):
                continue
            #print("Parsing file %s" % (path_file,))
            module_name = os.path.splitext(path_file)[0]
            spec = importlib.machinery.PathFinder().find_spec(module_name,[PathFolder])
            if not spec:
                continue
            file.append({'name': module_name, 'spec': spec.loader})
        return file
class ImportFile():
    def import_file(self,PathFolder):
        a = file_Route()
        files = a.get_file(PathFolder)
        members = []
        for rule_module in files:
            module = rule_module['spec'].load_module()
            members.append(module)

        
        for member in members:
            for name, data in inspect.getmembers(member):
                if name.startswith('__'):
                    continue
                print('{} : {!r}'.format(name, data))
                name_class.append(name)
                object_class.append(data)

        i = 0
        j = 0
        aux = -2
        for a in vet_meth: 
                num = vet_ref[i] #vai pegar o numero da referencia para achar a classe associada
                for b in vet_ref:
                    if num == b:
                        if aux != num:
                            aux = num #para não ter repetição de nome de classe
                            name_class.append(vet_class[j])
                i = i + 1
        #print(name_class)
class ArrangeVet():
#método para separar o vetor do codigo Kirby
    def transf_vet(self,vet): 
        list_vet = []
        i = 0
        lis = []
        for syn in vet:
            lis = vet[i].split(' ')
            for syn2 in lis:
                if syn2 != "":
                    list_vet.append(syn2)
                    #print(syn2)      
            i = i + 1
        return list_vet

class DiceVector():
#colocando na lista os vetores do código Kirby
    def Kirby(self):
        a = ArrangeVet()
        vetor_meth = nlp.vetorMetodo
        listWord.extend(a.transf_vet(vetor_meth)) #lista de metodos
        #print(listWord)

        vetor_par = nlp.vetorParametro
        listParameter.extend(a.transf_vet(vetor_par)) #lista de parametros 
        #print(listParameter)

    def isNumber(self,value): #verifica se a string passada é um numero
        try:
            int(value)
            float(value)
            return True
        except:
            return False

    def return_parameter(self,func): #retorna os parâmetros das classes da pasta cod
        return inspect.getargspec(func).args

    #criando o Map do nome do método com a sua respectiva lista de parâmetro. 'None' se não existir parâmetro.
    def transf_Map(self,list_Meth1,list_Meth2,list_Par2): #list_Meth1: lista de métodos das classes da pasta cod,listMeth2:lista de métodos do codigo Kirby, listPar2: lista de parametros do listMeth2
        dices = DiceVector()
        i = -1
        j = -1
        metadados_met = {} 
        for a in list_Meth1:
            i = i + 1
            parameter = dices.return_parameter(list_Object[i])
            met2 = {list_Meth1[i] : parameter}
            metadados_met.update(met2)
        for b in list_Meth2: #adc parâmetros do cod Kirby
            j = j + 1
            met2 = {list_Meth2[j] : list_Par2[j]}
            metadados_met.update(met2)
        #print(metadados_met.items())
        return metadados_met

    def create_list(self,lista,list_Object,classe):#função para criar lista de objetos dos métodos da classe passado por parâmetro
        for k,v in inspect.getmembers(classe): 
              if k.startswith('__')==False:
                    #print (k,v) 
                    lista.append(k) 
                    list_Object.append(v)

class DiceMap():     
    def transf_list(self):
        dices = DiceVector()
        arrange = ArrangeVet()
        for classe in object_class: #percorre a lista de objetos da classe
            dices.create_list(lista,list_Object,classe)
            #print(classe)
      
        listAux = lista + listWord
        listFinalMeth.extend(listAux) #lista com todos os métodos juntos
        #print(listFinalMeth)
    
        listFinalPar = []
    
        i = 0
        metadados = dices.transf_Map(lista,listWord,listParameter)
        #print(metadados)
        for a in listFinalMeth:  #lista com todos os parâmetros juntos
            aux = metadados[listFinalMeth[i]]
            listFinalPar.append(aux) 
            i = i + 1
        #print(listFinalPar)
        #arrumando a lista(listFinalPar) separadando por indices
        i = 0
        for a in listFinalPar:
            if dices.isNumber(a):
                resp = a
                parameters.append(resp)
            else:
                for b in listFinalPar[i]:
                    parameters.append(b)
            i = i + 1 
        #print(parameters)

    def compareMethods(self,syn1,syn2,selection): #faz a comparação de todos os métodos
        i = 0
        resp = 0
        for a in listFinalMeth:
            wn = FuncWordNet()
            calc = wn.SelectFunction(selection,syn1,listFinalMeth[i])
            if calc != 1: #se as strings forem iguais não conta, pois chegou no indice em que ela se encontra
                if calc > resp:
                    resp = calc
            i = i + 1
        return resp

    def compareParameter(self,syn,metadados,parameters,selection): #faz a comparação do parâmetro passado
        dice = DiceVector()
        i = 0
        j = 0
        resp = 0
        parameter_syn = metadados[syn]
        if dice.isNumber(parameter_syn): 
            for a in parameters:
                wn = FuncWordNet()
                calc = wn.SelectFunction(selection,parameter_syn,parameters[i])
                if calc != 1: #se as strings forem iguais não conta, pois chegou no indice em que ela se encontra
                    if calc > resp:
                        resp = calc
                i = i + 1
        else:
            for b in parameter_syn:
                for a in parameters:
                    wn = FuncWordNet()
                    calc = wn.SelectFunction(selection,b,a)
                    if calc != 1: #se as strings forem iguais não conta, pois chegou no indice em que ela se encontra
                        if calc > resp:
                            resp = calc
        return resp

    def qtd_meth(self,i): #função que conta a qtd de metodos de uma classe
        conte = 0
        for k,v in inspect.getmembers(object_class[i]): 
              if k.startswith('__')==False:
                    conte = conte + 1
        return conte

    #cod Kirby
    def qtd_meth2(self,i,vet_ref):
        conte = 0
        for a in vet_ref:
            if i == a:
                conte = conte + 1
        return conte

class AccountMethods():
    def account_meth(self): #função para contar o número de métodos
        dicesMap = DiceMap()
        tam_meth = []
        i = 0
        for a in object_class:
            tam_meth.append(dicesMap.qtd_meth(i))
            i = i + 1
        i = 0
        aux = -2 #para não ter repetição
        for a in vet_ref: 
            num = vet_ref[i]
            if aux != num:
                if num!= -1:
                    resp = dicesMap.qtd_meth2(num,vet_ref)
                    tam_meth.append(resp)
                    aux = num
            i = i + 1
        return tam_meth

class MethodClass():
    #função que associa os métodos a classe usando o Map
    def meth_class(self):
        a = AccountMethods()
        dices = DiceVector()
        tam_meth = []
        tam_meth.extend(a.account_meth())
        metadados = dices.transf_Map(lista,listWord,listParameter)
        metadados_met = {}
        values = [] #para colocar todos os metodos
    
        for key in metadados.items():
            #print("key: {}".format(key))
            values.append(key)
        #print(values)
        list_Meth = [] #para colocar os metodos que tem a classe com o mesmo nome
        j = 0 
        k = 0
        for c in name_class: #vai percorrer o nome das classes
            i = 0
            name = c #nome da classe
            #print(name)
            if tam_meth[k] > 1: #se for maior que 1 quer dizer que essa classe tem mais de um metodo
                while i < tam_meth[k]:
                    list_Meth.append(values[j])
                    #print("values[j]: {}".format(values[j]))
                    j = j + 1
                    i = i + 1
                metadados_met[name] = list_Meth
                #dados = {'class': name, 'methods/parameters': list_Meth}
                #metadados_met[name] = dados
                list_Meth = []
            else:
                #dados = {'class': name, 'methods/parameters': values[j]}
                #metadados_met[name] = dados
                metadados_met[name] = values[j]
                j = j + 1
            k = k + 1
        #print("metadados_met.items(): {}".format(metadados_met.items()))
        return metadados_met

class Similarity():
    def calc_similarity(self,Wmethods,Wparameters,selection):
        #print("Wmethods: {} Wparameters: {}".format(Wmethods,Wparameters))
        dicesMap = DiceMap()
        dices = DiceVector()
        i = 0
        j = 0
        resp = 0
        calc = 0
        conta = -1 #contador para achar o indice na 'lista'
        palavra1 = "" #synset da resposta
        palavra2 = "" #synset da resposta
        for syn1 in listWord:
            for syn2 in lista:   
                conta = conta + 1
                if conta == 0: #esse if é para chamar esse método(transf_Map) apenas uma vez, senão chama toda rodada do for
                    metadados = dices.transf_Map(lista,listWord,listParameter) #esse é o map dos métodos associados ao seus parâmetros
                    #print(metadados)
                print(syn1)
                print(syn2)
                lev = nltk.edit_distance(syn1, syn2) #comparar se as palavras são parecidas usando Levenshtein
                if lev > 1: 
                    #irá calcular a similaridade de acordo com a escolha do usuario
                    #percorro as listas e verifico qual é a maior similaridade
                    wn = FuncWordNet()
                    calc = wn.SelectFunction(selection,listWord[i],lista[j])
                    print(calc)
                    if(calc > resp):
                        resp = calc
                        palavra1 = listWord[i]
                        palavra2 = lista[j]
                else:
                    meth = dicesMap.compareMethods(syn1,syn2,selection) #ira comparar todos os metodos com o syn passado
                    #print("methods: {}".format(meth))
                    par1 = float(dicesMap.compareParameter(syn1,metadados,parameters,selection))
                    par2 = float(dicesMap.compareParameter(syn2,metadados,parameters,selection))
                    #print("par1: {}".format(par1))
                    #print("par2: {}".format(par2))
                    if Wmethods == -1 and Wparameters == -1:
                        calc1 = 0.4*meth + 0.6*par1
                        calc2 = 0.4*meth + 0.6*par2
                    else:
                        calc1 = Wmethods*meth + Wparameters*par1
                        calc2 = Wmethods*meth + Wparameters*par2

                    if calc1 > calc2:
                        resp = calc1
                        print(calc1)
                        palavra1 = syn1
                        palavra2 = syn2
                    else:
                        resp = calc2
                        print(calc2)
                        palavra1 = syn1
                        palavra2 = syn2
                calc = 0
                j = j + 1
            i = i + 1
            j = 0
            print('result: ')
            print(resp)
            if palavra1 == "" and palavra2 == "":
                continue
            else:
                print(palavra1)
                print(palavra2)
        print("listWord: {}".format(listWord))
        print("lista: {}".format(lista))

class DictList(dict):
    #tratamento de exceção para chaves / valores repetidos em um Map
    def __setitem__(self, key, value):
        try:
            self[key].append(value)
        except KeyError: 
            super(DictList, self).__setitem__(key, value)
        except AttributeError: 
            super(DictList, self).__setitem__(key, [self[key], value])

class FileClass():
    def file_class(self,pathKirby):
        m = MethodClass()
        dados = m.meth_class()
        map_dados = DictList()
        for nameObject in object_class:
            name_file.append(inspect.getfile(nameObject))
        conte = 0
        for dado in dados.items():
            conte = conte + 1
    
        i = 0
        for a in dados.items():
            if(i<conte-1):
                aux = {'file':name_file[i],'class':a}
                #print(aux)
                map_dados[name_file[i]] = aux
                i = i + 1
            else:
                aux = {'file':pathKirby,'class':a}
                #print(aux)
                map_dados[pathKirby] = aux
                i = i + 1
        #print("kirby: {}".format(pathKirby))
        print(map_dados.items())
        return map_dados
    def groupParameters(self):
        dices = DiceVector()
        i = 0
        j = 0
        for a in lista:
            parameter = dices.return_parameter(list_Object[i])
            Finalparameters.append(parameter)
            i = i + 1
        for b in listWord: #adc parâmetros do cod Kirby
            Finalparameters.append(listParameter[j])
            j = j + 1