#data loading
import pandas as pd
import numpy as np

#viz tools
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

#ml data preprocessing
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

#over and undersampling
from imblearn.under_sampling import RandomUnderSampler
from imblearn.pipeline import Pipeline, make_pipeline

#catboost classification model
from catboost import CatBoostClassifier

#for saving the trained model
from joblib import Parallel, delayed
import joblib

#main method
def train_model():
    #loading in data
    X = pd.read_csv("/users/n/Tempe_Traffic_V.2/X_input_data.csv")
    y = pd.read_csv("/users/n/Tempe_Traffic_V.2/y_label_data.csv")

    #catboost works natively with indices so we must make sure to specify which indices are categorical
    categorical_features_indices = np.where(X.dtypes != float)[0]

    #simple train test split, to fit our initial model
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

    #undersample our imbalanced majority class
    rs = RandomUnderSampler()
    x_under_train, y_under_train = rs.fit_resample(X = x_train, y = y_train)

    #creating our model with catboost
    model = CatBoostClassifier(cat_features = categorical_features_indices)

    #fitting the model
    model_fitted = model.fit(x_under_train, y_under_train)

    #saving our train and test data splits for latter
    x_train.to_csv("/users/n/Tempe_Traffic_V.2/x_train.csv", index=False)
    x_test.to_csv("/users/n/Tempe_Traffic_V.2/x_test.csv", index=False)
    y_train.to_csv("/users/n/Tempe_Traffic_V.2/y_train.csv", index=False)
    y_test.to_csv("/users/n/Tempe_Traffic_V.2/y_test.csv", index=False)

    return model_fitted

model_fitted = train_model()

#saving our trained model as a pickel file
joblib.dump(model_fitted, '/users/n/Tempe_Traffic_V.2/catboost_traffic_train_model.pkl')
