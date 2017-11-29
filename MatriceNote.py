import pandas as pd
import numpy as np
from io import StringIO
don_ratings = pd.read_csv("ml-latest-small/ratings.csv")
X = np.asarray(don_ratings)
don_Movie = pd.read_csv("ml-latest-small/movies.csv")
UserId = [elt for elt in don_ratings.userId]
MovieId = [elt for elt in don_ratings.movieId]
Rating = [elt for elt in don_ratings.rating]
M_IdMovie = [elt for elt in don_Movie.movieId] #Tout mes film par id
M_Film_User_Note = [[None for j in range(len(M_IdMovie))] for i in range(UserId[-1]+1)] #Matrice global qui contien les notes (None si film pas note)
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



def IdFilm(i):
    return M_IdMovie.index(i)


for i in range(len(M_note)):
    for j in range(len(M_note[i])):
        M_Film_User_Note[i+1][IdFilm(M_id[i][j])] = M_note[i][j]

def retrouve_note(id_user,id_film):
    if (id_film in M_id[id_user]) == True:
        return M_note[id_user][M_id[id_user].index(id_film)]
    else:
        print("film non noté")
        return False







