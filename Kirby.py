import spacy


nlp = spacy.load('en_core_web_sm')

palavrasArquivo = []

vetorfrase=[]

vetorReferenciaMetodoClasse = []
vetorReferenciaAtributoClasse = []
vetorReferenciaParametroMetodo=[]
vetorReferenciaValorAtributo = []


vetorGiven=[]
vetorWhen=[]
vetorThen=[]
vetorAnd=[]
vetorParametro=[]

vetorClasse = []
vetorMetodo = []
vetorAtributo = []
vetorValorAtributo = []





arquivo = open('caso01.txt', 'r')
contadorClasse=0
contadorMetodo = 0
contadorParametro=0
contadorAtributo = 0

ran=False

b=[]
for linha in arquivo:
    linha = linha.strip()
    palavrasArquivo.append(linha)
arquivo.close
for words in palavrasArquivo:
    doc = nlp(words)

    if words.split(" ").__contains__("Given") or words.split(" ").__contains__("Then") or words.split(" ").__contains__("When") or words.split(" ").__contains__("And"):
        vetorfrase.append(words)





for x in range(len(vetorfrase)):

    if(vetorfrase[x].__contains__("Given")):
        vetorGiven.append(vetorfrase[x])
    elif (vetorfrase[x].__contains__("When")):
        vetorWhen.append(vetorfrase[x])
    elif (vetorfrase[x].__contains__("Then")):
        vetorThen.append(vetorfrase[x])
    elif (vetorfrase[x].__contains__("And")):
        vetorAnd.append(vetorfrase[x])



possuiAtributo=False
ran=False
valor=""
metadeAtributo=""
possuiAtributo=False
percorreu=False
possuiClasse=False
for x in range(len(vetorGiven)):
    vetaux=vetorGiven[x].split(" ")


    for y in vetaux:

        if y.__contains__('"'):
            b = y.split('"')
            if vetorClasse.__contains__(b[1]):
                possuiClasse=True
                continue
            elif not possuiClasse and (not ran )and (not percorreu):
                vetorClasse.append(b[1])
                ran=True
            percorreu=True

            if b[1].isdecimal() or b[1] == "True" or b[1] == "False" and percorreu and possuiClasse and  (not vetorClasse.__contains__(b[1])):
                valor=b[1]
            elif percorreu and (not vetorClasse.__contains__(b[1])) :
                possuiAtributo=True
                vetorAtributo.append(b[1])
                vetorReferenciaAtributoClasse.append(contadorClasse)
                contadorAtributo+=1

    if valor!="":
        if not possuiAtributo:
            vetorAtributo.append(vetorClasse[contadorClasse])
            vetorReferenciaAtributoClasse.append(contadorClasse)
            contadorAtributo+=1
        vetorValorAtributo.append(valor)
        vetorReferenciaValorAtributo.append(contadorAtributo-1)

    ran=False
    valor=""
    vetaux=vetorWhen[x].split()
    possuiAtributo=False
    for y in vetaux:
        if y.__contains__('"'):
            b=y.split('"')
            if not ran:
                vetorMetodo.append(b[1])
                vetorReferenciaMetodoClasse.append(contadorClasse)
                ran=True

            else:
                vetorParametro.append(b[1])
                vetorReferenciaParametroMetodo.append(contadorMetodo)
                contadorMetodo+=1
                contadorParametro += 1

    ran = False
    valor = ""
    vetaux = vetorThen[x].split()
    possuiAtributo = False
    for y in vetaux:
        if y.__contains__('"'):
            b=y.split('"')

            vetorAtributo.append(vetorAtributo[contadorAtributo-1])
            vetorReferenciaAtributoClasse.append(contadorClasse)
            contadorAtributo+=1
            vetorValorAtributo.append(b[1])

    ran = False
    valor = ""
    possuiAtributo = False
    contadorClasse+=1
    possuiClasse=False
    percorreu=False


print("classe:")
print(vetorClasse)
print("metodo")
print(vetorMetodo)
print("referencia metodo a classe")
print(vetorReferenciaMetodoClasse)
print("Parametros")
print(vetorParametro)
print("referencia parametros")
print(vetorReferenciaParametroMetodo)
print("atributo")
print(vetorAtributo)
print("referencia atributo a Classe")
print(vetorReferenciaAtributoClasse)
print("valor atributo")
print(vetorValorAtributo)