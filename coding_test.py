#%%

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# %%
# 1

data = pd.read_csv('sales_data.txt')
data['revenue'] = data['quantity_sold'] * data['unit_price']
data_grouped = data.groupby(['store_id']).agg('sum').reset_index()
data_grouped
#%%
print('store id with highest total revenue:')
data_grouped['store_id'].iloc[0]


#%%
data_products = data.groupby('product_id').agg('sum').reset_index().sort_values(by='quantity_sold',ascending=False)
data_products.iloc[0]['product_id']

#%%

data.sort_values(by = 'revenue',ascending=False)

#%%



# 2
names = ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Fiona', 'Grace', 'Henry', 'Ivy', 'Jack','Katherine', 'Liam', 'Mia', 'Noah', 'Olivia', 'Peter', 'Quinn', 'Rachel', 'Sam', 'Taylor']

ages = [22, 20, 23, 21, 25, 24, 22, 19, 20, 21, 23, 22, 20, 21, 24, 19, 20, 22, 21, 23]

genders = ['Female', 'Male', 'Male', 'Male', 'Female', 'Female', 'Female', 'Male', 'Female', 'Male','Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Non-Binary', 'Female', 'Male', 'Non-Binary']



names
data = pd.DataFrame({
    'names':names,
    'ages':ages,
    'genders':genders,
})
data
#%%
plt.hist(data['ages'])

# %%
# 3

data_scores = pd.read_csv('scores_data.txt')

data_scores

# data_scores.groupby('')

# data_scores.melt().query("variable != 'student_id'").groupby('variable').agg('mean').reset_index()
data_long = data_scores.melt(id_vars=['student_id'])
data_long

#%%


print('mean subject scores:')
data_long.groupby('variable').agg('mean').reset_index()

#%%
print('highest median score:')
data_long.groupby('variable').agg('median').sort_values(by = 'value',ascending=False).iloc[0]


#%%
data_long.drop(['variable'],axis=1).groupby(['student_id']).agg('sum').reset_index().sort_values(by='value',ascending=False)


#%%
# 4
data_missing = pd.read_csv('missing_data.txt')

data_missing['age'] = data_missing['age'].fillna(data_missing['age'].mean())
data_missing['score'] = data_missing['score'].fillna(data_missing['score'].mean())
data_missing


# %%
# 5

X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
# y = 1 * x_0 + 2 * x_1 + 3
y = np.dot(X, np.array([1, 2])) + 3


#%%

study_hours = np.array([2, 3, 1, 4, 5, 2, 3, 4, 5, 6]).reshape((-1, 1))
exam_scores = np.array([65, 70, 60, 75, 85, 70, 72, 82, 88, 92])
exam_scores
plt.plot(study_hours, exam_scores)


#%%

reg = LinearRegression().fit(study_hours, exam_scores)
reg.score(study_hours, exam_scores)
reg

#%%
reg.coef_
reg.intercept_
reg.predict(np.array([[6]]))


#%%
study_hours
exam_scores


# %%
