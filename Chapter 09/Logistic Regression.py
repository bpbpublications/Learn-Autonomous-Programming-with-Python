

from sklearn.datasets import load_iris  
import pandas as pd
iris = load_iris()
df = pd.DataFrame(iris.data,columns=iris.feature_names)
df['target'] = iris.target
print(df)

from sklearn.datasets import load_iris  
import pandas as pd
iris = load_iris()
X = iris.data[:100]
Y = iris.target[:100]

from sklearn.linear_model import LogisticRegression
LR = LogisticRegression()
LR.fit(X,Y)

X_predict = [6.3,2.5,4.3,1.5]
Y_predict = LR.predict([X_predict])
print(Y_predict)

from sklearn.model_selection import train_test_split
X_Train, X_Test,Y_Train, Y_Test = train_test_split(X,Y, test_size=0.3, random_state=100)

LR.fit(X_Train,Y_Train)
Y_Predict = LR.predict([X_Test[23]])

print('X_Test:' + str(X_Test[23]))
print('Y_Test:' + str(Y_Test[23]))
print('Y_Predict:' + str(Y_Predict))

