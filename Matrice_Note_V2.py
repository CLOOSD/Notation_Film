from Dico import index_movie #import de la fonction qui prend en entre l'id du film et ressort son index dans la matrice
import pandas as pd
import numpy as np
import scipy.sparse as sp
from sklearn.metrics import mean_squared_error
from math import sqrt
from scipy.sparse.linalg import svds
from sklearn.decomposition import NMF
don_ratings = pd.read_csv("ml-latest-small/ratings.csv")
don_Movie = pd.read_csv("ml-latest-small/movies.csv")
UserId = [elt for elt in don_ratings.userId]
MovieId = [elt for elt in don_ratings.movieId]
Rating = [elt for elt in don_ratings.rating]
M_IdMovie = [elt for elt in don_Movie.movieId] #Tout mes film par id
M_Film_User_Note = np.asarray([[-1.0 for j in range(len(M_IdMovie))] for i in range(UserId[-1]+1)]) #Matrice global qui contien les notes (None si film pas note)
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
        M_Film_User_Note[i+1][index_movie(M_id[i][j])] = float( M_note[i][j])

def Notes(id_User,id_Movie):
    return (M_Film_User_Note[id_User][index_movie(id_Movie)])


#On a bien une Matrice[id_de_l'utilisateur][id_du_film] cette matrice donne la note du film si le film est noté et -1 si le film n'est pas noté cette matrice est un array numpy
M_Dysn_Thri = []
M_id_Nom = {}
def Matrice_D_T(id_Movie,nouvelle_id ,nom_film):
    M_Dysn_Thri.append([])
    M_Dysn_Thri.append(0)
    M_id_Nom[nouvelle_id] = nom_film
    for i in range(672):
        M_Dysn_Thri[nouvelle_id].append(Note(i,id_Movie))


Matrice_D_T(1029,0,"Dumbo")
Matrice_D_T(1940,2,"Fantasia")
Matrice_D_T(596,2,"Pinocchio")
Matrice_D_T(74089,3,"Peter Pan")
Matrice_D_T(588,4,"Aladin")
Matrice_D_T(2018,5,"Bambi")
Matrice_D_T(81591,6,"Black Swan")
Matrice_D_T(594,7,"Blanche Neige")
Matrice_D_T(1022,8,"Cendrillon")
Matrice_D_T(364,9,"Le Roi Lion")
Matrice_D_T(1367,10,"Dalmatiens")
Matrice_D_T(616,11,"Aristochats")
Matrice_D_T(1023,12,"Winnie L'ourson")
Matrice_D_T(8961,13,"Indestructible")
Matrice_D_T(2080,14,"La belle et les clocha")
Matrice_D_T(47,15,"Seven")
Matrice_D_T(112556,16,"Gone Girl")
Matrice_D_T(50,17,"Usual Suspects")
Matrice_D_T(296,18,"Pulp Fiction")
Matrice_D_T(2959,19,"Fight Club")
Matrice_D_T(58559,20,"Batman the Dark knight")
Matrice_D_T(79132,21,"Inception")
Matrice_D_T(74458,22,"Shutter Island")
Matrice_D_T(1089,23,"Reservoir Dogs")
Matrice_D_T(97304,24,"Argo")

Matrice_D_T = np.asarray(Matrice_D_T)


def rmse(prediction, ground_truth):
    prediction = prediction[ground_truth.nonzero()].flatten()
    ground_truth = ground_truth[ground_truth.nonzero()].flatten()
    return sqrt(mean_squared_error(prediction, ground_truth))


#get SVD components from train matrix. Choose k.
u, s, vt = svds(M_Film_User_Note, k = 100)
s_diag_matrix=np.diag(s)
X_pred = np.dot(np.dot(u, s_diag_matrix), vt)
print ('User-based CF MSE: ' + str(rmse(X_pred, M_Film_User_Note)))


model = NMF(n_components=2, init='random', random_state=0)
W = model.fit_transform(M_note)
#H = model.components_
print(W)

