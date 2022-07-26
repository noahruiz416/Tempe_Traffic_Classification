#this script contains visualizations besides the ones from the google collab notebook
#in particular this script pertains to the model itself

#data loading
import pandas as pd
import numpy as np

#viz tools
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.pyplot import figure
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import RocCurveDisplay


#importing our model
from joblib import Parallel, delayed
import joblib

#loading our trained model
model_fitted_joblib = joblib.load('/users/n/Tempe_Traffic_V.2/catboost_traffic_train_model.pkl')

#loading our test data
x_test = pd.read_csv("/users/n/Tempe_Traffic_V.2/x_test.csv")
y_test = pd.read_csv("/users/n/Tempe_Traffic_V.2/y_test.csv")

#loading train data
x_train = pd.read_csv("/users/n/Tempe_Traffic_V.2/x_train.csv")

#visualization for feature importance on test data
cb_features = model_fitted_joblib.feature_importances_
plt.barh(x_test.columns, sorted(model_fitted_joblib.feature_importances_))
plt.title("Catboost Most Important Features On Train Data")
plt.xlabel("Shap Value")
figure(figsize=(40, 20), dpi=500)

#on train data
gb_features = model_fitted_joblib.feature_importances_
plt.barh(x_test.columns, sorted(model_fitted_joblib.feature_importances_))
plt.title("Catboost Most Important Features On Test Data")
plt.xlabel("Shap Value")
figure(figsize=(40, 20), dpi=500)

#visulization for confusion ConfusionMatrix on test data
ConfusionMatrixDisplay.from_estimator(model_fitted_joblib, x_test, y_test)
plt.title("Confusion Matrix")

#visualization for ROC Curve on test data
RocCurveDisplay.from_estimator(model_fitted_joblib, x_test, y_test)
plt.title("ROC Curve")
