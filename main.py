import pandas as pd
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values       #x = Years of exp; take all rows and columns except last
y = dataset.iloc[:,1].values          #y = Salary; take all rows and columns with index 1

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3, random_state=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)

import matplotlib.pyplot as plt
plt.scatter(X_test, y_test, color = 'black')
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

new_salary_pred = regressor.predict([[15]])
print('Predicted salary of person with 15 years of experience:', new_salary_pred)
new_salary_pred = regressor.predict([[20]])
print('Predicted salary of person with 15 years of experience:', new_salary_pred)
