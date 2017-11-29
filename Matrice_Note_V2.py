from Dico import index_movie #import de la fonction qui prend en entre l'id du film et ressort son index dans la matrice
import pandas as pd
import numpy as np
don_ratings = pd.read_csv("ml-latest-small/ratings.csv")
don_Movie = pd.read_csv("ml-latest-small/movies.csv")
UserId = [elt for elt in don_ratings.userId]
MovieId = [elt for elt in don_ratings.movieId]
Rating = [elt for elt in don_ratings.rating]
M_IdMovie = [elt for elt in don_Movie.movieId] #Tout mes film par id
M_Film_User_Note = np.asarray([[-1 for j in range(len(M_IdMovie))] for i in range(UserId[-1]+1)]) #Matrice global qui contien les notes (None si film pas note)
M_note = [] #Matrice qui contient 671 vecteur (1 vecteur 1 personne) avec chaque note des film noter par l'user
M_id = []


j = 0
UserId.append(672)
for i in range(672):
    M_note.append([])
    M_id.append([])
    while UserId[j] == i:
        M_note[i].append(Rating[j])
        M_id[i].append(MovieId[j])
        j += 1
del M_note[0]
del M_id[0]

M_note = np.asarray(M_note)
M_id = np.asarray(M_id)

for i in range(len(M_note)):
    for j in range(len(M_note[i])):
        M_Film_User_Note[i+1][index_movie(M_id[i][j])] = M_note[i][j]

#On a bien une Matrice[id_de_l'utilisateur][id_du_film] cette matrice donne la note du film si le film est noté et -1 si le film n'est pas noté cette matrice est un array numpy
