from nltk.corpus import wordnet as wn 

def similarityLCH(word1,word2):
    vet = [wn.NOUN,wn.VERB,wn.ADJ,wn.ADV] #vetor de substantivo,verbo,adjetivo e adverbio
    i = 0
    calc = 0
    resp = 0
    while i < 4: #vai percorrer todos os elementos do vet(substantivo,verbo,adjetivo e adverbio)
        synset1 = wn.synsets(word1,vet[i])
        synset2 = wn.synsets(word2,vet[i])  
        #verifica qual o maior calculo das similaridades
        for syn1 in synset1:
            for syn2 in synset2:
                calc = syn1.lch_similarity(syn2)
                if calc > resp:
                    resp = calc
                calc = 0
        i = i+1 
        return resp

def similarityWUP(word1,word2):
    vet = [wn.NOUN,wn.VERB,wn.ADJ,wn.ADV]
    i = 0
    calc = 0
    resp = 0
    while i<4:
        synset1 = wn.synsets(word1,vet[i])
        synset2 = wn.synsets(word2, vet[i])
        for syn1 in synset1:
            for syn2 in synset2:
                calc = syn1.wup_similarity(syn2)
                if calc > resp:
                    resp = calc
                calc = 0
        i = i + 1
        return resp
    
def similarityPATH(word1,word2):
    vet = [wn.NOUN,wn.VERB,wn.ADJ,wn.ADV]
    i = 0
    calc = 0
    resp = 0
    while i < 4:
        synset1 = wn.synsets(word1,vet[i])
        synset2 = wn.synsets(word2,vet[i])  
        for syn1 in synset1:
            for syn2 in synset2:
                calc = syn1.path_similarity(syn2)
                if calc > resp:
                    resp = calc
                calc = 0
        i = i+1 
        return resp
    
def similarityRES(word1,word2):
    from nltk.corpus import wordnet_ic
    brown_ic = wordnet_ic.ic('ic-brown.dat')
    vet = [wn.NOUN,wn.VERB,wn.ADJ,wn.ADV]
    i = 0
    calc = 0
    resp = 0
    while i < 4:
        synset1 = wn.synsets(word1,vet[i])
        synset2 = wn.synsets(word2,vet[i])  
        for syn1 in synset1:
            for syn2 in synset2:
                calc = syn1.res_similarity(syn2, brown_ic)
                if calc > resp:
                    resp = calc
                calc = 0
        i = i+1 
        return resp
    
def similarityJCN(word1,word2):
    from nltk.corpus import wordnet_ic
    brown_ic = wordnet_ic.ic('ic-brown.dat')
    vet = [wn.NOUN,wn.VERB,wn.ADJ,wn.ADV]
    i = 0
    calc = 0
    resp = 0
    while i < 4:
        synset1 = wn.synsets(word1,vet[i])
        synset2 = wn.synsets(word2,vet[i])  
        for syn1 in synset1:
            for syn2 in synset2:
                calc = syn1.jcn_similarity(syn2, brown_ic)
                if calc > resp:
                    resp = calc
                calc = 0
        i = i+1 
        return resp

def similarityLIN(word1,word2):
    from nltk.corpus import wordnet_ic
    semcor_ic = wordnet_ic.ic('ic-semcor.dat')
    vet = [wn.NOUN,wn.VERB,wn.ADJ,wn.ADV]
    i = 0
    calc = 0
    resp = 0
    while i < 4:
        synset1 = wn.synsets(word1,vet[i])
        synset2 = wn.synsets(word2,vet[i])  
        for syn1 in synset1:
            for syn2 in synset2:
                calc = syn1.lin_similarity(syn2, semcor_ic)
                if calc > resp:
                    resp = calc
                calc = 0
        i = i+1 
        return resp