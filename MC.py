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
for (i in range(671)):

    
def IdFilm(i):
    return AllMovieId.index(i)

