

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score

iris = load_iris()
X = iris.data
Y = iris.target

X_Train, X_Test, Y_Train, Y_Test = train_test_split(X,Y,test_size=0.3, random_state=100)

DT_Model = DecisionTreeClassifier()
DT_Model.fit(X_Train,Y_Train)

Y_Predict = DT_Model.predict(X_Test)
accuracy = accuracy_score(Y_Predict, Y_Test)

print(accuracy)
