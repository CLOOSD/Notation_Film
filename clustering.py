import numpy as np
from sklearn.decomposition import NMF
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
#rom Matrice_Note_V2 import M_note, M_id #regarder je ne pense pas que je puisse importer des matrice au pire tester avec des fausses aux debut
X = np.array([[1, 1], [2, 1], [3, 1.2], [4, 1], [5, 0.8], [6, 1]]) #dans notre matrice cela corresponds aux films (dans la matrice films user)

model = NMF(n_components=2, init='random', random_state=0)
W = model.fit_transform(X)
H = model.components_


#on fait une PCA qui va nous permettre de reduire la taille de notre matrice de base
pca = PCA(n_components=2) #devra etre plus grand dans notre matrice
X_fit = pca.fit_transform(X)
#je ne sais pas si on en a besoin dans notre matrice
#X.shape[1]
#X_fit.shape[1]


#on fait le clustering par groupe de films
n_clusters = 3
kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(X_fit)
#sorted((kmeans.labels_))
label_X = list(zip(kmeans.labels_, X))
#print(sorted(label_X, ))
#type(list)

#print(label_X)
print(kmeans.labels_)
for i in range(n_clusters):
    print("cluster ", i)
    print(np.nonzero(kmeans.labels_ == i))