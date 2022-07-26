#this script will test our trained model with the other split of data

#data loading
import pandas as pd
import numpy as np

#for importing our trained model
from joblib import Parallel, delayed
import joblib

#basics to show performance on test set
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import RocCurveDisplay
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score

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

#loading data
x_test = pd.read_csv("/users/n/Tempe_Traffic_V.2/x_test.csv")
y_test = pd.read_csv("/users/n/Tempe_Traffic_V.2/y_test.csv")

#running our trained model on the test
model_fitted_joblib = joblib.load('/users/n/Tempe_Traffic_V.2/catboost_traffic_train_model.pkl')

#confusion matrix, from test data
ConfusionMatrixDisplay.from_estimator(model_fitted_joblib, x_test, y_test)

#ROC Curve from test data
RocCurveDisplay.from_estimator(model_fitted_joblib, x_test, y_test)

#running the metric scoring function
metric_scoring(model_fitted_joblib, x_test, y_test)
