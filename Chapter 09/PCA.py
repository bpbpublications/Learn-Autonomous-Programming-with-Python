

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data
Y = iris.target

X_Train, X_Test, Y_Train, Y_Test = train_test_split(X,Y,test_size=0.3, random_state=100)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_Train = sc.fit_transform(X_Train)
X_Test = sc.transform(X_Test)

from sklearn.decomposition import PCA
pca = PCA()
X_train = pca.fit_transform(X_Train)
X_test = pca.transform(X_Test)

explained_variance = pca.explained_variance_ratio_

print(explained_variance) 
