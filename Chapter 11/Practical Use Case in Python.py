
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from prefect import task, Flow

@task(nout=2)
def Load_Iris():
    iris = load_iris()
    X = iris.data
    Y = iris.target
    return X,Y

@task(nout=4)
def Split_Data(X,Y):
    X_Train, X_Test, Y_Train, Y_Test = train_test_split(X,Y,test_size=0.3, random_state=100)
    return X_Train, X_Test, Y_Train, Y_Test

@task
def Execute_Naive_Bayes(X_Train, X_Test, Y_Train, Y_Test):
    NB = GaussianNB()
    NB.fit(X_Train, Y_Train)
    Y_Predict_Test_Sample = NB.predict(X_Test)
    accuracy = accuracy_score(Y_Test, Y_Predict_Test_Sample)
    print('Accuracy:', accuracy)


with Flow('Execute-Naive-Bayes') as flow:
    X,Y = Load_Iris()
    X_Train, X_Test, Y_Train, Y_Test = Split_Data(X,Y)
    Execute_Naive_Bayes(X_Train, X_Test, Y_Train, Y_Test)
      
flow.run()
flow.visualize(filename="Execute-Naive-Bayes")
    
    
    
    
    
    
    
    


