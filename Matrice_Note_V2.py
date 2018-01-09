from Dico import index_movie, index_movie_2
#import de la fonction qui prend en entre l'id du film et ressort son index dans la matrice
import pandas as pd
import numpy as np
import scipy.sparse as sp
from sklearn.metrics import mean_squared_error
from math import sqrt
from scipy.sparse.linalg import svds
from sklearn.decomposition import NMF

import numpy as np
from sklearn.decomposition import NMF
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

from clustering import clustering
import numpy as np
from sklearn.decomposition import NMF
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

import random



#rom Matrice_Note_V2 import M_note, M_id #regarder je ne pense pas que je puisse importer des matrice au pire tester avec des fausses aux debut
#X = np.array([[1, 1], [2, 1], [3, 1.2], [4, 1], [5, 0.8], [6, 1]]) #dans notre matrice cela corresponds aux films (dans la matrice films user)




don_ratings = pd.read_csv("ml-latest-small/ratings.csv")
don_Movie = pd.read_csv("ml-latest-small/movies.csv")
don_Movie_2 = pd.read_csv("ml-latest-small/FichierMatrice.csv")
UserId = [elt for elt in don_ratings.userId]
MovieId = [elt for elt in don_ratings.movieId]
Rating = [elt for elt in don_ratings.rating]
M_IdMovie = [elt for elt in don_Movie.movieId]
M_IdMovie_2 = [elt for elt in don_Movie_2.movieId]      #Tout les film par id


x = np.random.normal(loc=2.5)
print(x)

M_Film_User_Note = np.asarray([[False for j in range(len(M_IdMovie))] for i in range(UserId[-1]+1)])
#Matrice global qui contien les notes (-1 si film pas note)
M_note = []     #Matrice qui contient 671 vecteur (1 vecteur 1 personne) avec chaque note des films note par l'user
M_id = []




M_Dysn_Thri = np.asarray([[False for j in range(UserId[-1]+1)] for i in range(len(M_IdMovie_2))])


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
        M_Film_User_Note[i+1][index_movie(M_id[i][j])] = float(M_note[i][j])
M_Film_Note_User = np.transpose(M_Film_User_Note)

def Notes(id_User,id_Movie):
    return (M_Film_User_Note[id_User][index_movie(id_Movie)])

#M_Dysn_Thri = np.asarray([[-1.0 for j in range(len(UserId[-1]+1))] for i in range(M_IdMovie_2)])

for elt in M_IdMovie_2:#Matrice contenant 25 films
    for i in range(672):
        M_Dysn_Thri[index_movie_2(elt)][i] = Notes(i,elt)

    
#On a bien une Matrice[id_de_l'utilisateur][id_du_film] cette matrice donne la note du film si le film est noté et -1 si le film n'est pas noté cette matrice est un array numpy






def rmse(prediction, ground_truth):
    prediction = prediction[ground_truth.nonzero()].flatten()
    ground_truth = ground_truth[ground_truth.nonzero()].flatten()
    return sqrt(mean_squared_error(prediction, ground_truth))
#c'est quoi ca ?


#get SVD components from train matrix. Choose k.
#u, s, vt = svds(M_Film_User_Note, k = 100)
#s_diag_matrix=np.diag(s)
#X_pred = np.dot(np.dot(u, s_diag_matrix), vt)
#print ('User-based CF MSE: ' + str(rmse(X_pred, M_Film_User_Note)))




#model = NMF(n_components=2, init='random', random_state=0)
#W = model.fit_transform(M_note)
#H = model.components_
#print(W)
#print (M_IdMovie_2)
#print(len(M_IdMovie_2))
#print((M_Dysn_Thri[4][3])) #4e film et 3e utilisateurs
#print(Notes(3,588))



if __name__ == '__main__':
    print("matreice dysthri : " ,M_Dysn_Thri)
    clustering(M_Film_Note_User)
    #M_test = clustering(M_IdMovie2)
    #index_movie_2(M_test)



