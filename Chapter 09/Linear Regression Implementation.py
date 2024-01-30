

from sklearn import linear_model
reg = linear_model.LinearRegression()

training_data = [[0], [3], [17], [23]]
labels = [0,9,51,69]

reg.fit(training_data, labels)

print(reg.coef_)
print(reg.intercept_)
