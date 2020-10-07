import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

from tabulate import tabulate

dataset = pd.read_csv('hiring.csv')
dataset['experience'].fillna(0, inplace=True)
dataset['test_score'].fillna(dataset['test_score'].mean(), inplace=True)

# all columns except salary, the dependent variable
X = dataset.iloc[:, :3]

def convertToInt(word):
    word_dict = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        'ten': 10,
        'eleven': 11,
        'twelve': 12,
        0:0
    }
    return word_dict[word]

X['experience'] = X['experience'].apply(lambda x: convertToInt(x))
print(tabulate(X, headers='keys', tablefmt='psql'))

y = dataset.iloc[:, -1]

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

regressor.fit(X, y)

pickle.dump(regressor, open('model.pkl', 'wb'))


