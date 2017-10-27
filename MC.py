import pandas as pd
import numpy as np
from io import StringIO
don_ratings = pd.read_csv("ml-latest-small/ratings.csv")
X = np.asarray(don_ratings)
don_Movie = pd.read_csv("ml-latest-small/movies.csv")
AllMovieId = [elt for elt in don_Movie.movieId]
UserId = [elt for elt in don_ratings.userId]
MovieId = [elt for elt in don_ratings.movieId]
Rating = [elt for elt in don_ratings.rating]

M_Coeur = [[0 for j in range(len(AllMovieId))] for i in range(UserId[-1]+1)]
M_idFix = []
M_IdMovie = [elt for elt in don_Movie.movieId]

j = 0
for i in range(671):
    M_idFix.append([])
    while UserId[i] == i+1:
        M_idFix[i].append(Rating[i])
        j += 1


def IdFilm(i):
    return M_IdMovie.index(i)

for i in range(671):
    for elt in M_idFix[i]:
        M_Coeur[i][IdFilm(elt)]


print(M_Coeur[610][IdFilm(55820)])