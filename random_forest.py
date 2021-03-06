import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from math import sqrt

pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', -1)

###################################################
loc = "total_003.csv"
dataset = pd.read_csv(loc)

Y = dataset[["career_len"]]
X = dataset[["total_duration","profit","average ride time","speed","average dist per ride","speed","10_to_6","9_to_5",'prime_time','weekend_per']]
print(X)
X_train, X_test, y_train, y_test = train_test_split(X,Y,test_size=0.2, random_state=123)

# print (X_train.shape)
# print (X_test.shape)
# print (Y_train.shape)
# print (Y_test.shape)

scaler = StandardScaler()
train_scaled = scaler.fit_transform(X_train)
test_scaled = scaler.transform(X_test)

tree_model = DecisionTreeRegressor()
rf_model = RandomForestRegressor()

tree_model.fit(train_scaled, y_train)
rf_model.fit(train_scaled, y_train)

# tree_mse = mean_squared_error(y_train, tree_model.predict(train_scaled))
# tree_mae = mean_absolute_error(y_train, tree_model.predict(train_scaled))
# rf_mse = mean_squared_error(y_train, rf_model.predict(train_scaled))
# rf_mae = mean_absolute_error(y_train, rf_model.predict(train_scaled))
#
# print("Decision Tree training mse = ",tree_mse," & mae = ",tree_mae," & rmse = ", sqrt(tree_mse))
# print("Random Forest training mse = ",rf_mse," & mae = ",rf_mae," & rmse = ", sqrt(rf_mse))
print(rf_model.predict(test_scaled).mean())

tree_test_mse = mean_squared_error(y_test, tree_model.predict(test_scaled))
tree_test_mae = mean_absolute_error(y_test, tree_model.predict(test_scaled))
rf_test_mse = mean_squared_error(y_test, rf_model.predict(test_scaled))
rf_test_mae = mean_absolute_error(y_test, rf_model.predict(test_scaled))

print("Decision Tree test mse = ",tree_test_mse," & mae = ",tree_test_mae," & rmse = ", sqrt(tree_test_mse))
print("Random Forest test mse = ",rf_test_mse," & mae = ",rf_test_mae," & rmse = ", sqrt(rf_test_mse))