

from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data
Y = iris.target

X_Train, X_Test, Y_Train, Y_Test = train_test_split(X,Y,test_size=0.3, random_state=100)

NB = GaussianNB()
NB.fit(X_Train, Y_Train)

Y_Predict = NB.predict([X_Test[5]])
print('Y_Predict:' + str(Y_Predict))
print('Y_Test:' + str(Y_Test[5]))

from sklearn.metrics import accuracy_score
Y_Predict_Test_Sample = NB.predict(X_Test)
accuracy = accuracy_score(Y_Test, Y_Predict_Test_Sample)
print('Accuracy:', accuracy)

