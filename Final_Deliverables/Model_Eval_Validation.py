#this script runs a stratified cross fold validation on the fitted model
#we do this on the train dataset in order to gain a better understanding of generalize performance

#this script will test our trained model with the other split of data

#data loading
import pandas as pd
import numpy as np

#for importing our trained model
from joblib import Parallel, delayed
import joblib

#basics to show performance on test set
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score

#cross validation
from imblearn.pipeline import Pipeline, make_pipeline
from sklearn.model_selection import cross_val_score
from sklearn.metrics import make_scorer
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_validate

#undersampling and catboost
from imblearn.under_sampling import RandomUnderSampler
from catboost import CatBoostClassifier

#this function computes important metrics for the test dataset
def metric_scoring(classifier, x_test_data, y_test_data):
  y_true = y_test_data
  y_pred = classifier.predict(x_test_data)
  precision = precision_score(y_true, y_pred)
  recall = recall_score(y_true, y_pred)
  accuracy = accuracy_score(y_true, y_pred)
  f1 = f1_score(y_true, y_pred)

  metric_data = {
      'Precision' : precision,
      'Recall' : recall,
      'Accuracy': accuracy,
      'F1 Score': f1
  }
  return metric_data

#loading in dataset
x_train = pd.read_csv("/users/n/Tempe_Traffic_V.2/x_train.csv")
y_train = pd.read_csv("/users/n/Tempe_Traffic_V.2/y_train.csv")

#pipeline combines the random undersampler and the catboost classifier, this allows for both steps to be done at once while
#also preventing data leakage or undersampled overfitting

#prepping indices
categorical_features_indices = np.where(x_train.dtypes != float)[0]

imba_pipeline = make_pipeline(RandomUnderSampler(),
                              CatBoostClassifier(cat_features = categorical_features_indices))

#scoring metrics for pipeline
scoring = {'accuracy' : make_scorer(accuracy_score),
           'precision' : make_scorer(precision_score),
           'recall' : make_scorer(recall_score),
           'f1_score' : make_scorer(f1_score)}

#number of k folds
stratKFold = StratifiedKFold(n_splits=5)

cross_validate(imba_pipeline, x_train, y_train, scoring=scoring, cv=stratKFold)
