"""
Web server script that exposes endpoints and pushes ship principal parameter data (csv file) to Redis for passenger
ship powering by model server. Polls Redis for response from model server.

Deployment is based on pretrained model developed using scikit learn
"""

#%%

import pandas as pd
import pickle
import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics

from sklearn.preprocessing import MinMaxScaler

import matplotlib.pyplot as plt

scaler = MinMaxScaler()


#%%
# Load data
df = pd.read_csv("../../Data/MonoROPAX_Training.csv").drop(['ID', 'D', 'Npax', 'Nveh', 'GT'], 1)


#%%

# preprocessing

dataset_scaled = scaler.fit_transform(df)
df_scaled = pd.DataFrame(dataset_scaled, index=df.index)
df_scaled.columns = ['LWL', 'B', 'T', 'L/B', 'B/T', 'Disp', 'CB', 'Vs', 'Fn', 'P']


#%%
X = df_scaled.drop(['P'], 1)
y = df_scaled['P']

#%%
save_model = 'mlp_pwr_best_model.sav'
loaded_model = pickle.load(open(save_model,'rb'))

#%%

prediction_mlp = loaded_model.predict(X)

print('MultiLayer Perceptron Regression (Train-80%, Test-20%)\n')
print('MAE:', metrics.mean_absolute_error(y, prediction_mlp))
print('MSE:', metrics.mean_squared_error(y, prediction_mlp))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y, prediction_mlp)))
print('Test score:', loaded_model.score(X, y))

#%%
