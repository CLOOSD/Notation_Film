import pandas as pd
import numpy as np
from io import StringIO
don_ratings = pd.read_csv("ml-latest-small/ratings.csv")
X = np.asarray(don_ratings)
don_Movie = pd.read_csv("ml-latest-small/movies.csv")
UserId = [elt for elt in don_ratings.userId]
MovieId = [elt for elt in don_ratings.movieId]
Rating = [elt for elt in don_ratings.rating]
M_IdMovie = [elt for elt in don_Movie.movieId]
M_Film_User_Note = [[None for j in range(len(M_IdMovie))] for i in range(UserId[-1]+1)] #Matrice global qui contien les notes (None si film pas note)
M_id = [] #Matrice qui contient 671 vecteur (1 vecteur 1 personne) avec chaque note des film noter par l'user


for i in range(671):
    M_id.append([])
    while UserId[i] == i+1:
        M_id[i].append(Rating[i])


def IdFilm(i):
    return M_IdMovie.index(i)

for i in range(671):
    for elt in M_idFix[i]:
        M_Coeur[i][IdFilm(elt)].append(elt)
