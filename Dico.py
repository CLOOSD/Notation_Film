import pandas as pd
import numpy as np
from io import StringIO
don_ratings = pd.read_csv("ml-latest-small/ratings.csv")
X = np.asarray(don_ratings)
don_Movie = pd.read_csv("ml-latest-small/movies.csv")
don_Movie_2 = pd.read_csv("ml-latest-small/FichierMatrice.csv")
UserId = [elt for elt in don_ratings.userId]
MovieId = [elt for elt in don_ratings.movieId]
Rating = [elt for elt in don_ratings.rating]
M_IdMovie = [elt for elt in don_Movie.movieId]
M_IdMovie_2 = [elt for elt in don_Movie_2.movieId]
M_Film_User_Note = [[None for j in range(len(M_IdMovie))] for i in range(UserId[-1]+1)] #Matrice global qui contien les notes (None si film pas note)
M_id = [] #Matrice qui contient 671 vecteur (1 vecteur 1 personne) avec chaque note des films noter par l'user


dict_MatriceToFilm = {}
dict_FilmtoMatrice = {}
for IdMovie,value in enumerate(M_IdMovie,1): #film est l'indice du film
    dict_FilmtoMatrice[IdMovie] = value
    dict_MatriceToFilm[value] = IdMovie
    #if film ==0:

dict_MatriceToFilm_2 = {}
for IdMovie_2,value in enumerate(M_IdMovie_2,1): #film est l'indice du film
    dict_MatriceToFilm_2[value] = IdMovie

def index_movie(id_film):
    return dict_MatriceToFilm[id_film]-1

def inder_movie_2(id_film):
    return dict_MatriceToFilm_2[id_film]-1
    #for elt in M_IdMovie:
        #for elt1 in film:
            #dict_MatriceToFilm[elt] = elt1
            #dict_FilmtoMatrice[elt1] = elt



#fonction prediction
#IdFilm.head()
