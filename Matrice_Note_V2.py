import pandas as pd
import numpy as np

from clustering import clustering
from Dico import index_movie, index_movie_2, nom_film ,ind_movie, ind_movie_2
#import de la fonction qui prend en entre l'id du film et ressort son index dans la matrice

import random


#importation et creation de matrice
don_ratings = pd.read_csv("ml-latest-small/ratings.csv")
don_Movie = pd.read_csv("ml-latest-small/movies.csv")
don_Movie_2 = pd.read_csv("ml-latest-small/FichierMatrice.csv")
UserId = [elt for elt in don_ratings.userId]            #Tout les iddentifiants des utilisateurs
MovieId = [elt for elt in don_ratings.movieId]          #Tout les films note par les users (aparait autant de fois que note)
Rating = [elt for elt in don_ratings.rating]            #Notes
M_IdMovie = [elt for elt in don_Movie.movieId]          #Tout les film par id
M_IdMovie_2 = [elt for elt in don_Movie_2.movieId]      #Liste contenant nos films tests


x = np.random.normal(loc=2.5)           #Creation de bruit
print(x)

M_Film_User_Note = np.asarray([[False for j in range(len(M_IdMovie))] for i in range(UserId[-1]+1)])
#Matrice global qui contien les notes (False si le film n'est pas note)
M_note = []     #Mliste qui contient 671 vecteur (1 vecteur 1 personne) avec chaque note des films note par l'utilisateur
M_id = []       #Id des films




M_Dysn_Thri = np.asarray([[False for j in range(UserId[-1]+1)] for i in range(len(M_IdMovie_2))])
#Matrice de test (pour le clustering) contenant des films disney ainsi que des thrillers


#creation d'une liste de lise ou chaque sous liste correpond a chaques film note par un user
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

#Convertion en array numpy des listes crees
M_note = np.asarray(M_note)
M_id = np.asarray(M_id)


#creation de nos matrices globales
for i in range(len(M_note)):
    for j in range(len(M_note[i])):
        M_Film_User_Note[i+1][index_movie(M_id[i][j])] = float(M_note[i][j])
M_Film_Note_User = np.transpose(M_Film_User_Note)

def Notes(id_User,id_Movie):
    """
    Fonction retournant les notes des films
    :param id_User: id de l'utilisateur (int)
    :param id_Movie: id du film (int)
    :return: La note correspondant a l'user et le film (int)
    """
    return (M_Film_User_Note[id_User][index_movie(id_Movie)])


for elt in M_IdMovie_2:         #Matrice contenant 25 films
    for i in range(672):
        M_Dysn_Thri[index_movie_2(elt)][i] = Notes(i,elt)

    
#On a une Matrice[id_de_l'utilisateur][id_du_film]. Cette matrice donne la note du film si le film
# est noté et False si le film n'est pas noté cette matrice est un array numpy

def id_tofilm_test(clust):
    """
    Transforme les numéro contenue dans le clustering_test en le nom des films
    :param clust: le clustering_test effectuer sur le test (array)
    :return: Une list de list avec les nom des films au lieux des numéro des index des films (array)
    """
    clust_nom = []
    for i in range(len(clust)):
        clust_nom.append([])
        for j in range(np.size(clust[i][0])):
            clust_nom[i].append(nom_film(ind_movie_2(clust[i][0][j])))
    return clust_nom

def id_tofilm(clust):
    """"
    Transforme les numéro contenue dans le clustering en le nom des films
    :param clust: le clustering effectuer sur le test (array)
    :return: Une list de list avec les nom des films au lieux des numéro des index des films (array)
    """
    clust_nom = []
    for i in range(len(clust)):
        clust_nom.append([])
        for j in range(np.size(clust[i][0])):
            clust_nom[i].append(nom_film(ind_movie(clust[i][0][j])))
    return clust_nom

if __name__ == '__main__':
    #print("matreice dysthri : " ,M_Dysn_Thri)
    #cluster = clustering(M_Dysn_Thri)
    #print(id_tofilm_test(cluster))
    cluster_big = clustering(M_Film_Note_User)
    print(id_tofilm(cluster_big))
    #M_test = clustering(M_IdMovie2)
    #index_movie_2(M_test)
    #print(M_IdMovie_2)


