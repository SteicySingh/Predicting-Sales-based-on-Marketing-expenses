import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import *
from sklearn.preprocessing import *
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Load the data from the Excel file
data = pd.read_excel('/Users/steicysingh/Desktop/Spring 2023/INST737/Final Project/Final Model/Dataset.xlsx')

# Print the data
print(data)

# Select the columns to be scaled (in this example, columns A, B, C)
cols_to_scale = ['TV', 'Radio', 'SocialMedia']

# Initialize the scaler object
scaler = MinMaxScaler()  # or StandardScaler()

# Fit and transform the selected columns using the scaler object
data[cols_to_scale] = scaler.fit_transform(data[cols_to_scale])

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data[cols_to_scale], data['Sales'], test_size=0.2, random_state=42)

# Print the shapes of the training and testing sets
print("Training set shape:", X_train.shape, y_train.shape)
print("Testing set shape:", X_test.shape, y_test.shape)

# Initialize the linear regression model
model = LinearRegression()

# Fit the model to the training data
model.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = model.predict(X_test)

# Calculate the mean squared error
mse = mean_squared_error(y_test, y_pred)

# Calculate the mean absolute error
mae = mean_absolute_error(y_test, y_pred)

# Calculate the R-squared value
r2 = r2_score(y_test, y_pred)

# Print the evaluation metrics
print("Mean Squared Error:", mse)
print("Mean Absolute Error:", mae)
print("R-squared Value:", r2)

# Trying to use the Model
# Load the new data into a new DataFrame
new_data = pd.read_excel('/Users/steicysingh/Desktop/Spring 2023/INST737/Final Project/Final Model/New Data.xlsx')

# Scale the new data using the same scaler object
new_data[cols_to_scale] = scaler.transform(new_data[cols_to_scale])

# Use the model to make predictions on the new data
new_predictions = model.predict(new_data[cols_to_scale])

# Add the RowNumber column to the new_predictions array
new_predictions = np.column_stack((new_data['RowNumber'], new_predictions))

# Print the predicted values or store them in a new column in the DataFrame
print(new_predictions)










