

import pandas as pd
import numpy as np

df = pd.read_csv(r"IPL_Auction_2022_FullList.csv")
df = df[['Specialism','Test caps','ODI caps','T20 caps','IPL','Bid']]

mapping_dictionary ={'ALL-ROUNDER' : 0, 'BATSMAN' : 1, 'BOWLER' : 2, 'WICKETKEEPER':3}
df['Specialism'] = df['Specialism'].map(mapping_dictionary)

X = df.drop('Bid',axis=1).values
Y = df['Bid'].values

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

X_Train, X_Test, Y_Train, Y_Test = train_test_split(
 			X, Y, test_size = 0.3, random_state=100)
LR = LogisticRegression()
LR.fit(X,Y)

from sklearn.metrics import accuracy_score
Y_Predict = LR.predict(X_Test)
accuracy = accuracy_score(Y_Test, Y_Predict)
print('Accuracy:', accuracy)

from sklearn.metrics import confusion_matrix
tn, fp, fn, tp = confusion_matrix(Y_Test, Y_Predict).ravel()
print('True Negative:' + str(tn), 'False Positive:' + str(fp), 'False Negative:' + str(fn), 'True Positive:' + str(tp))
