import pandas as pd

don_Movie = pd.read_csv("ml-latest-small/movies.csv")
don_Movie_2 = pd.read_csv("ml-latest-small/FichierMatrice.csv")
M_IdMovie = [elt for elt in don_Movie.movieId]
M_IdMovie_2 = [elt for elt in don_Movie_2.movieId]
M_Nom = [elt for elt in don_Movie.title]

dict_MatriceToFilm = {}
dict_FilmtoMatrice = {}
dict_idFilmtoNom = {}

for IdMovie,value in enumerate(M_IdMovie,1): #film est l'indice du film
    dict_FilmtoMatrice[IdMovie] = value
    dict_MatriceToFilm[value] = IdMovie
    #if film ==0:

for i in range(len(M_Nom)): #film est l'indice du film
    dict_idFilmtoNom[M_IdMovie[i]] = M_Nom[i]

dict_MatriceToFilm_2 = {}
dict_FilmtoMatrice_2 = {}
for IdMovie_2,value in enumerate(M_IdMovie_2,1): #film est l'indice du film
    dict_MatriceToFilm_2[value] = IdMovie_2
    dict_FilmtoMatrice_2[IdMovie_2] = value

def index_movie(id_film):
    return dict_MatriceToFilm[id_film]-1

def index_movie_2(id_film):
    return dict_MatriceToFilm_2[id_film]-1

def ind_movie(id):
    return dict_FilmtoMatrice[id+1]

def ind_movie_2(id):
    return dict_FilmtoMatrice_2[id+1]

def nom_film(id_film):
    return dict_idFilmtoNom[id_film]
