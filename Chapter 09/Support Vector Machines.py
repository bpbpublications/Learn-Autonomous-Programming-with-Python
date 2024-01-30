

from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris


iris = load_iris()
X = iris.data
Y = iris.target

X_Train, X_Test, Y_Train, Y_Test = train_test_split(X,Y,test_size=0.3, random_state=100)

SVC_Model = SVC(kernel = 'linear', random_state = 0)
SVC_Model.fit(X_Train,Y_Train)
Y_Predict = SVC_Model.predict(X_Test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_Test, Y_Predict)
print(cm)


