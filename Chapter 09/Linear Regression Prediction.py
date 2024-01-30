# Importing necessary libraries
from sklearn import linear_model
import numpy as np

# Create an instance of the Linear Regression model
reg = linear_model.LinearRegression()

# Define training data and corresponding labels
# Training data represents the independent variables
training_data = np.array([[0],[3],[17],[23]])

# Labels are the dependent variable (output) for each training data point
labels = np.array([0,9,51,69])

# Train the model using the training data and labels
reg.fit(training_data, labels)
# Define testing data for which we want to predict the output
testing_data = np.array([[21],[13],[15]])

# Use the trained model to make predictions on the testing data
output = reg.predict(testing_data)

# Print the predicted output
print(output)

