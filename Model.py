# -*- coding: utf-8 -*-
"""main.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12qXg0plu3nCnpSeHRuOsXyC9C9NYjxtC
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv("output1.csv")
df2 = pd.read_csv("output2.csv")
df3 = pd.read_csv("output3.csv")
df10 = pd.read_csv("output10.csv")
df20 = pd.read_csv("output20.csv")
df30 = pd.read_csv("output30.csv")
dftest = pd.read_csv("test1.csv")
df4 = pd.read_csv("output1 copy.csv")
df40 = pd.read_csv("output2 copy.csv")

df1.info()

df1.describe()

df2.describe()

df3.describe()

"""
13
14
7
8"""

df10.describe()

df20.describe()

df30.describe()

df1.drop(df1.columns[[16, 17, 18, 19]], axis = 1, inplace = True)
df2.drop(df2.columns[[16,17,18, 19]], axis=1, inplace=True)
df3.drop(df3.columns[[16,17,18, 19]], axis=1, inplace=True)
df4.drop(df4.columns[[16,17,18, 19]], axis=1, inplace=True)
df10.drop(df10.columns[[16,17,18, 19]], axis=1, inplace=True)
df20.drop(df20.columns[[16,17,18, 19]], axis=1, inplace=True)
df30.drop(df30.columns[[16,17,18, 19]], axis=1, inplace=True)
df40.drop(df40.columns[[16,17,18, 19]], axis=1, inplace=True)

df1.columns

df1.head()

eeg_columns = df4.columns[:16]

df4['Label'] = 'Meditation'

time_unit = 2  # 1 unit = 2 seconds
num_data_points = len(df4)
time = np.arange(num_data_points) * time_unit

plt.figure(figsize=(12, 4))
for column in eeg_columns:
    data = df4[column]
    plt.plot(time, data, label=column)

plt.title('EEG Channels')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

# plt.legend()
plt.grid(True)

plt.show()

eeg_columns = df40.columns[:16]

df40['Label'] = 'Stress'

time_unit = 2  # 1 unit = 2 seconds
num_data_points = len(df40)
time = np.arange(num_data_points) * time_unit

plt.figure(figsize=(12, 4))
for column in eeg_columns:
    data = df40[column]
    plt.plot(time, data, label=column)

plt.title('EEG Channels')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

# plt.legend()
plt.grid(True)

plt.show()

eeg_columns = df1.columns[:16]

df1['Label'] = 'Stress'

time_unit = 2  # 1 unit = 2 seconds
num_data_points = len(df1)
time = np.arange(num_data_points) * time_unit

plt.figure(figsize=(12, 4))
for column in eeg_columns:
    data = df1[column]
    plt.plot(time, data, label=column)

plt.title('EEG Channels')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

# plt.legend()
plt.grid(True)

plt.show()

eeg_columns = df2.columns[:16]

df2['Label'] = 'Meditation'

time_unit = 2  # 1 unit = 2 seconds
num_data_points = len(df2)
time = np.arange(num_data_points) * time_unit

plt.figure(figsize=(12, 4))
for column in eeg_columns:
    data = df2[column]
    plt.plot(time, data, label=column)

plt.title('EEG Channels')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

# plt.legend()
plt.grid(True)

plt.show()

eeg_columns = df3.columns[:16]

df3['Label'] = 'Meditation'

time_unit = 2  # 1 unit = 2 seconds
num_data_points = len(df3)
time = np.arange(num_data_points) * time_unit

plt.figure(figsize=(12, 4))
for column in eeg_columns:
    data = df3[column]
    plt.plot(time, data, label=column)

plt.title('EEG Channels')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

# plt.legend()
plt.grid(True)

plt.show()

eeg_columns = df10.columns[:16]

df10['Label'] = 'Stress'

time_unit = 2  # 1 unit = 2 seconds
num_data_points = len(df10)
time = np.arange(num_data_points) * time_unit

plt.figure(figsize=(12, 4))
for column in eeg_columns:
    data = df10[column]
    plt.plot(time, data, label=column)

plt.title('EEG Channels')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

# plt.legend()
plt.grid(True)

plt.show()

eeg_columns = df20.columns[:16]

df20['Label'] = 'Meditation'

time_unit = 2  # 1 unit = 2 seconds
num_data_points = len(df20)
time = np.arange(num_data_points) * time_unit

plt.figure(figsize=(12, 4))
for column in eeg_columns:
    data = df20[column]
    plt.plot(time, data, label=column)

plt.title('EEG Channels')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

# plt.legend()
plt.grid(True)

plt.show()

eeg_columns = df30.columns[:16]

df30['Label'] = 'Stress'

time_unit = 2  # 1 unit = 2 seconds
num_data_points = len(df30)
time = np.arange(num_data_points) * time_unit

plt.figure(figsize=(12, 4))
for column in eeg_columns:
    data = df30[column]
    plt.plot(time, data, label=column)

plt.title('EEG Channels')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

# plt.legend()
plt.grid(True)

plt.show()

data_model = [df1,df2,df3,df10,df20,df30, df4, df40]
dataset = pd.concat(data_model)

dataset.reset_index(drop=True, inplace=True)

dataset.info()

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from imblearn.over_sampling import RandomOverSampler


# Separate the features and target variable
x = dataset.drop(["Label"], axis =1).values
y = dataset["Label"].values

# Perform 80-20 train-test split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

#print shape of all above define
print("Shape of x_train: ", x_train.shape)
print("Shape of x_test: ", x_test.shape)
print("Shape of y_train: ", y_train.shape)
print("Shape of y_test: ", y_test.shape)

ros = RandomOverSampler(random_state=42)
x_train_resampled, y_train_resampled = ros.fit_resample(x_train, y_train)

dftest = dftest.drop(dftest.columns[[-1,-2,-3,-4]], axis=1)

dftest.head()

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import ConfusionMatrixDisplay, confusion_matrix


k = 3  # Set the value of k
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(x_train, y_train)
y_pred = knn.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

cm = confusion_matrix(y_test,y_pred)
dist = ConfusionMatrixDisplay(cm)
dist.plot()
plt.show()

lr = LogisticRegression()
lr.fit(x_train, y_train)
y_pred = lr.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.4f}')

cm = confusion_matrix(y_test,y_pred)
dist = ConfusionMatrixDisplay(cm)
dist.plot()
plt.show()

from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
vc=DecisionTreeClassifier(criterion='gini',max_depth=4,random_state=5)
vc.fit(x_train,y_train)
y_pred=vc.predict(x_test)


print(metrics.accuracy_score(y_test,y_pred))

cm = confusion_matrix(y_test,y_pred)
dist = ConfusionMatrixDisplay(cm)
dist.plot()
plt.show()

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, ConfusionMatrixDisplay
from sklearn.model_selection import RandomizedSearchCV, train_test_split
from scipy.stats import randint

# Tree Visualisation
from sklearn.tree import export_graphviz
from IPython.display import Image
import graphviz

rf = RandomForestClassifier()
rf.fit(x_train, y_train)

y_pred = rf.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

cm = confusion_matrix(y_test,y_pred)
dist = ConfusionMatrixDisplay(cm)
dist.plot()
plt.show()

from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
target_label = label_encoder.fit_transform(y_train)

test_label = label_encoder.fit_transform(y_test)

params ={
    'max_depth': [3, 4, 5, 6, 8, 10, 12, 15],
    'learning_rate': [0.05,0.10,0.15,0.20,0.25,0.30],
    'n_estimators': [100, 200,300,400,500,600,900,1000,2000,4000,5000],
    'colsample_bytree': [0.3,0.4,0.5,0.7],
    'gamma':[0.0,0.1,0.2,0.3,0.4],
    'min_child_weight': [1,3,5,7,8],
    'subsample':[0.5,0.6,0.7,0.8,0.9,1],
    'reg_alpha':[0, 0.001, 0.01, 0.03, 0.08, 0.3, 0.5],
    'reg_lambda':[0, 0.001, 0.01, 0.03, 0.08, 0.3, 0.5],
    'scale_pos_weight':[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1],
    'max_delta_step':[0,1,2,3,4,5,6,7,8,9,10],
    'base_score': [0.5,0.7,0.9]
}

from xgboost import XGBClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import RandomizedSearchCV,GridSearchCV
# from sklearn.model_selection import GridSearchCV
xgb_tunned =XGBClassifier()
# bagging = BaggingClassifier(xgb_tunned)
xgb_tunned.fit(x_train, target_label)

y_pred = xgb_tunned.predict(x_test)

accuracy = accuracy_score(test_label, y_pred)
print("Accuracy:", accuracy)


cm = confusion_matrix(test_label,y_pred)
dist = ConfusionMatrixDisplay(cm)
dist.plot()
plt.show()

