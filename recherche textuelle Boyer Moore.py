################################ Ne pas modifier ############################


def text_file_to_string(fichier):
    '''
    Renvoie une chaine de caratères à partir d'un fichier txt
    '''
    texte = open(fichier,'r')
    res =""
    for l in texte.readlines():
        res += l
    return res

def affiche_nb_occurences(fichier,motif,BS,MC):
    texte = text_file_to_string(fichier)
    print("Dans ",fichier," on trouve ",len(recherche_Boyer_Moore(texte,motif,BS,MC))," occurence du motif : ",motif)

def alphabet(texte):
    return list(set(texte))

###########################################################################

def pretraitement_BS(motif:str)->list[int]:
    '''
    Renvoie le tableau Bon Suffixe du motif donné
    '''
    m = len(motif)
    p = 0
    for i in range(m):
        if motif[0:i]==motif[m-i:m]:
            p = m-i+1
    
    BS = [1 for i in range(m)]
    
    for i in range(m-2,-1,-1):
        val = p
        for k in range(i):
            if motif[i+1:m]==motif[k:k+m-i-1] and motif[k-1]!=motif[i]:
                val = i-k+1
        BS[i]=val
        
    return BS



def pretraitement_MC(motif:str,alphabet:list[chr])->dict[int]:
    '''
    Renvoie le tableau Mauvais Caractère à partir du motif et de l'alphabet donnés
    '''
    MC = {}
    for c in alphabet:
        MC[c]=len(motif)
    for i in range(len(motif)-1):
        MC[motif[i]]=len(motif)-i-1
    return MC



def recherche_Boyer_Moore(texte:str ,motif:str, BS:list[int], MC:dict[int] ) -> list[int]: 
    '''
    Renvoie la liste des occurences d'un motif dans un texte
    '''
    n = len(texte)
    m = len(motif)
    position = []
    i = 0
    while i < n-m :
        j = m-1
        while j>=0 and texte[i+j]==motif[j]: 
            j += -1
        if j == -1:
            position.append(i)
            i += BS[0]
        else:
            i += max(BS[j],MC[texte[i+j]]+j-m+1)
            
    return(position) 



        
        


fichier1 = 'ADN.txt'
fichier2 = 'Le-seigneur-des-anneaux-tome-1.txt'
fichier3 = 'Frank Herberts Dune Saga Collection Books 1 - 6.txt'

motif1 = "CCTGCT"
alphabet1 = alphabet(text_file_to_string(fichier1))
motif2 = "Sam"
alphabet2 = alphabet(text_file_to_string(fichier2))
motif3 = "Fremen"
alphabet3 = alphabet(text_file_to_string(fichier3))

         
affiche_nb_occurences(fichier1,motif1,pretraitement_BS(motif1),pretraitement_MC(motif1,alphabet1))
affiche_nb_occurences(fichier2,motif2,pretraitement_BS(motif2),pretraitement_MC(motif2,alphabet2))
affiche_nb_occurences(fichier3,motif3,pretraitement_BS(motif3),pretraitement_MC(motif3,alphabet3))

