import pandas as pd

dataframe = pd.read_csv('vw.csv')
dataframe = dataframe[dataframe['model'] == ' Golf']
dataframe.pop('model')
dataframe.to_csv('used_cars.csv', index=False)
