def evolution(grille):
    nb_ligne = 0
    grille1 = grille
    for ligne in grille:
        nb_element = 0
        for element in ligne:
            if nb_ligne == 0:
                if nb_element == 0:
                    voisins = [grille[nb_ligne][nb_element + 1], grille[nb_ligne + 1][nb_element], grille[nb_ligne + 1][nb_element + 1]]
                elif nb_element == len(ligne) - 1:
                     voisins = [grille[nb_ligne][nb_element - 1], grille[nb_ligne + 1][nb_element], grille[nb_ligne + 1][nb_element - 1]]
                else:
                    voisins = [grille[nb_ligne][nb_element - 1], grille[nb_ligne][nb_element + 1], grille[nb_ligne + 1][nb_element - 1], grille[nb_ligne + 1][nb_element], grille[nb_ligne + 1][nb_element + 1]]
                        
            elif nb_ligne == len(grille) - 1:
                if nb_element == 0:
                    voisins = [grille[nb_ligne][nb_element + 1], grille[nb_ligne - 1][nb_element], grille[nb_ligne - 1][nb_element - 1]]
                elif nb_element == len(ligne) - 1:
                    voisins = [grille[nb_ligne][nb_element - 1], grille[nb_ligne - 1][nb_element], grille[nb_ligne - 1][nb_element - 1]]
                else:
                    voisins = [grille[nb_ligne][nb_element - 1], grille[nb_ligne][nb_element + 1], grille[nb_ligne - 1][nb_element - 1], grille[nb_ligne - 1][nb_element], grille[nb_ligne - 1][nb_element + 1]]
            elif nb_element == 0:
                voisins = [grille[nb_ligne - 1][nb_element], grille[nb_ligne - 1][nb_element + 1], grille[nb_ligne][nb_element + 1], grille[nb_ligne + 1][nb_element], grille[nb_ligne + 1][nb_element + 1]]
            elif nb_element == len(ligne) - 1:
                voisins = [grille[nb_ligne - 1][nb_element], grille[nb_ligne - 1][nb_element - 1], grille[nb_ligne][nb_element - 1], grille[nb_ligne + 1][nb_element], grille[nb_ligne + 1][nb_element - 1]]
            else:
                voisins = [grille[nb_ligne - 1][nb_element - 1], grille[nb_ligne - 1][nb_element], grille[nb_ligne - 1][nb_element + 1], grille[nb_ligne][nb_element - 1], grille[nb_ligne][nb_element + 1], grille[nb_ligne + 1][nb_element - 1], grille[nb_ligne + 1][nb_element], grille[nb_ligne + 1][nb_element + 1]]
            if element == 1:
                print(voisins)
                if voisins.count(1) != 2 and voisins.count(1) != 3:
                    grille1[nb_ligne][nb_element] = 0
            else:
                if voisins.count(1) == 3:
                    grille1[nb_ligne][nb_element] = 1
            nb_element += 1
        nb_ligne += 1
    return grille1

grille1 = [[0,0,0,0,0], [0,0,0,0,0], [0,1,1,1,0], [0,0,0,0,0], [0,0,0,0,0]]

print(evolution(grille1))
                
                