

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data
Y = iris.target

X_Train, X_Test, Y_Train, Y_Test = train_test_split(
			X, Y, test_size = 0.3, random_state=100)

knn = KNeighborsClassifier(n_neighbors=12)
knn.fit(X_Train, Y_Train)

Y_Predict = knn.predict([X_Test[15]])
print('Y_Predict:' + str(Y_Predict))
print('Y_actual:' + str(Y_Test[15]))
