#a. Read the provided CSV file ‘data.csv’.
#b. https://drive.google.com/drive/folders/1h8C3mLsso-R-sIOLsvoYwPLzy2fJ4IOF?usp=sharing
#c. Show the basic statistical description about the data.
#d. Check if the data has null values.
#i. Replace the null values with the mean
#e. Select at least two columns and aggregate the data using: min, max, count, mean.
#f. Filter the dataframe to select the rows with calories values between 500 and 1000.
#g. Filter the dataframe to select the rows with calories values > 500 and pulse < 100.
#h. Create a new “df_modified” dataframe that contains all the columns from df except for
#Maxpulse”.
#i. Delete the “Maxpulse” column from the main df dataframe
#j. Convert the datatype of Calories column to int datatype.
#k. Using pandas create a scatter plot for the two columns (Duration and Calories)

import pandas as pandas

import pandas as pd
df = pd.read_csv("data.csv")
df.describe()

"""# New Section"""

null_values = df.isnull().sum()
#is null is to identify null values
print(null_values)

df.fillna(df.mean(), inplace=True)
#fillna is to fill the null position
print(df)

df = df[["Duration", "Pulse" ]]

agg_dict = {"Duration": ["max", "min", "count", "mean"],
            "Pulse": ["max", "min", "count", "mean"]}
agg_df = df.agg(agg_dict)
print(agg_df)

df = pd.read_csv("data.csv")
Calories_filter = (df["Calories"] >= 500) & (df["Calories"] <= 1000)
filtered_df = df[Calories_filter]
print(filtered_df)

df = pd.read_csv("data.csv")
Calories_filter = (df["Calories"] > 500) & (df["Pulse"] < 100)
filtered_df = df[Calories_filter]
print(filtered_df)

df_modified = df.drop(columns=["Maxpulse"])
print(df_modified)

df['Calories'] = df['Calories'].fillna(0).astype(int)
print(df)

import matplotlib.pyplot as plt

df.plot(kind='scatter', x='Duration', y='Calories', figsize=(6,3))
plt.show()

import pandas as pd
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

salariesData = pd.read_csv('Salary_Data.csv') #importing data from the CSV file

#splitting the data in to training and testing
X = salariesData.iloc[:, :-1].values
Y= salariesData.iloc[:, 1].values

#splitting 1/3 of the data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 1/3, random_state = 0)

# Fitting Simple Linear Regression to the training set
reg = LinearRegression()
reg.fit(X_train, Y_train)

# Predicting the Test set result
pred = reg.predict(X_test)

# Calculating the Mean_squared_error
mse = mean_squared_error(Y_test, pred)

#Visualising the Training set results and Test set results
plt.scatter(X_train, Y_train, color = 'blue')
plt.scatter(X_test, Y_test, color = 'red')
plt.title('Salary Data')
plt.xlabel('Experience (Years)')
plt.ylabel('Salary')
plt.show()
