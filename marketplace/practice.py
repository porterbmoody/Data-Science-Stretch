#%%
import pandas as pd
import tensorflow as tf
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import colors
import matplotlib as mat
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import sys
sys.path.append("..")
from DataUtility.DataUtility import DataUtility

path = 'cars.csv'
data = pd.read_csv(path)

data

#%%
data1 = data.copy()



data1 = clean_data(data1)

data1['doors'] = data['title']
data1
#%%.

def run_regressor(data, x_columns, y_columns):
    X = data[x_columns].values.reshape(-1, 1)
    y = data[y_columns]
    model = LinearRegression()
    model.fit(X, y)

    y_predictions = model.predict(X)
    r2_score = model.score(X, y)

    plt.scatter(X, y)
    plt.scatter(X, y)
    plt.plot(X, y_predictions, color='red')
    plt.title('R2 = ' + str(r2_score))
    plt.show()

    return model


model = run_regressor(data1, 'mileage', 'price')



#%%

makers = [
    'Toyota',
    'Volkswagen',
    'Tesla',
    'Ford',
    'Volvo',
    'Honda',
    'BMW',
    'Hyundai',
    'Audi',
    'Volkswagen',
    'Pontiac',
    'alero',
    'Kia',
    'Lexus',
    'Chevrolet',
    'Mitsubishi',
    'Nissan',
    'Porsche',
    'Buick',
    'Mazda',
    'Mercedes',
    'Jeep',
    'Subaru',
    'Dodge',
    'Chrysler',
    'Geo',
    'Suzuki',
    'Acura',
    'Infiniti',
    'Rivian',
    'GMC',
    'Jaguar',
    'MINI',
    'Mercury',
    'Ram',
    'Cadillac',
    'Scion',
    'Fiat',
    'Axial',
    ]

data1['make'] = data1['title'].str.findall('|'.join(makers))

data1 = data1.explode(['make'])

data1.groupby(['make']).agg('count').reset_index().sort_values(by=['title'], ascending=False)

# data1 = data1.dropna(subset = ['make', 'price'], how = 'any')
#%%

agg_dict = {
    'price': ['min', 'mean', 'median','max', 'count'],
    # 'mileage': 'mean'
}
data1.groupby(['make']).agg(agg_dict).reset_index()

#%%

data1[['make', 'price']].groupby(['make']).agg('count').reset_index().sort_values(by=['price'])

#%%
import tensorflow as tf
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential

model = Sequential()
model.add(Dense(32, activation='relu', input_shape = (1,)))
model.add(Dense(1, activation='softmax'))


model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

model.summary()

#%%

num_epochs = 50

history = model.fit(
    data1['mileage'], 
    data1['price'], 
    epochs=num_epochs
    )


#%%
test_data = ... # Load and preprocess test data
test_loss, test_acc = model.evaluate(test_data)

predictions = model.predict(test_data)


# %%

x = np.arange(1,20).reshape(-1,1)
y = 2*x + np.random.randint(-1, 1, size = len(x)).reshape(-1,1)

print(x)
print(y)
plt.scatter(x, y)


#%%

# Create and fit the linear regression model
model = LinearRegression()
model.fit(x, y)
model.score(x, y)

#%%

# Predictions
# X_new = np.array([6]).reshape(-1, 1)
# predicted_y = model.predict(X_new)

# Plotting
plt.scatter(x, y, label='Actual Data')
plt.plot(x, model.predict(x), color='red', label='Regression Line')
# plt.scatter(X_new, predicted_y, color='green', label='Predicted Value')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()

# %%

model = Sequential([
    Dense(4, input_shape=(1,), activation='ReLU')
    # Dense(4, input_shape=(1,), activation='')
])

model.compile(optimizer='adam', loss='mean_squared_error')

model.summary()
# %%

history = model.fit(x, y, epochs = 500, verbose=1)
history

#%%
plt.plot(history.history['loss'])

# plt.scatter(X, y, label='Actual Data')
# plt.plot(X, model.predict(X), color='red', label='NN Prediction')
# plt.scatter(X_new, predicted_y, color='green', label='Predicted Value')
# plt.xlabel('X')
# plt.ylabel('y')
# plt.legend()
# plt.show()
# %%
model.predict(np.array([4, 5]))


# %%
import numpy as np
from sklearn.linear_model import LinearRegression
X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
# y = 1 * x_0 + 2 * x_1 + 3
y = np.dot(X, np.array([1, 5]))

print(X)
print(y)

#%%
reg = LinearRegression().fit(X, y)
reg.score(X, y)
reg.coef_
reg.intercept_
reg.predict(np.array([[3, 5]]))

