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

def affiche_nb_occurences(fichier,motif):
    texte = text_file_to_string(fichier)
    print("Dans ",fichier," on trouve ",len(recherche_naive(texte,motif))," occurence du motif ",motif)

###########################################################################

def recherche_naive(texte:str ,motif:str ) -> list[int]: 
    '''
    Revoie la liste des occurenes d'un motif dans un texte
    '''
    response = []
    t = len(texte)
    m = len(motif)
    for i in range(0, t - m + 1):
        if texte[i:i + m] == motif:
           response.append(i)
    return response
            




fichier1 = 'ADN.txt'
fichier2 = 'Le-seigneur-des-anneaux-tome-1.txt'
fichier3 = 'Frank Herberts Dune Saga Collection Books 1 - 6.txt'

motif1 = "CCTGCT"
motif2 = "Sam"
motif3 = "Fremen"
              
            
affiche_nb_occurences(fichier1,motif1)
affiche_nb_occurences(fichier2,motif2)
affiche_nb_occurences(fichier3,motif3)

