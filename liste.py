import pandas as pd
don_ratings = pd.read_csv("ml-latest-small/ratings.csv")
don_Movie = pd.read_csv("ml-latest-small/movies.csv")
AllMovieId = [elt for elt in don_Movie.movieId]
UserId = [elt for elt in don_ratings.userId]
UserId1 = [elt for elt in don_ratings.userId]
MovieId = [elt for elt in don_ratings.movieId]
Rating = [elt for elt in don_ratings.rating]
Matrice1 = [[0 for i in range(len(AllMovieId))] for i in range(UserId1[-1])]
Matrice = [[]]
UserId.append(0)
j = 0
Matrice = [0]
for i in range(672):
    Matrice.append({})
    while (UserId[j] == i):
        Matrice[i][MovieId[j]] = Rating[j]
        j += 1
print(Matrice[671])
print(len(Matrice1))
print(len(Matrice1[34]))