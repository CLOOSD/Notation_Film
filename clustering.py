import numpy as np
from sklearn.decomposition import NMF
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans



def clustering(X):
    model = NMF(n_components=1, init='random', random_state=0)
    W = model.fit_transform(X)
    #print(W)
    H = model.components_


    #on fait une PCA qui va nous permettre de reduire la taille de notre matrice de base
    pca = PCA(n_components=2)           #devra etre plus grand dans notre matrice
    X_fit = pca.fit_transform(X)


    #on fait le clustering par groupe de films
    n_clusters = 100
    kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(X_fit)


    M_cluster= []
    label_X = list(zip(kmeans.labels_, X))
    print(kmeans.labels_)
    for i in range(n_clusters):
        print("cluster ", i)
        print(np.nonzero(kmeans.labels_ == i))
        M_cluster.append(np.nonzero(kmeans.labels_ == i))

    return np.asarray(M_cluster)








