# Model card for City of Tempe Accident Data 

Sections and prompts from the [model cards paper](https://arxiv.org/abs/1810.03993), v2.

Jump to section:

- [Model details](#model-details)
- [Intended use](#intended-use)
- [Factors](#factors)
- [Metrics](#metrics)
- [Evaluation data](#evaluation-data)
- [Training data](#training-data)
- [Quantitative analyses](#quantitative-analyses)
- [Ethical considerations](#ethical-considerations)
- [Caveats and recommendations](#caveats-and-recommendations)

## Model details

- Person or organization developing model: Noah Ruiz, ASU Unit for Data Science & Analytics

- Model date: 
  7/25/22
  
- Model version: 
  - 1.0
 
- Final Model type: 
  - Catboost Classification Model

- Information about training algorithms, parameters, fairness constraints or other applied
  approaches, and features:   
  - Data is collected from the City of Tempe public records regarding traffic accidents from 2012 - 2020
  - Around 21 different features are included within the model, with a large majority being engineered in order to reduce dimensionality
  - A high imbalance exists within the dataset for fatal and nonfatal accidents which is most likely due to the rare occurence of such events 
 
- Paper or other resource for more information:
  - Data Source: https://data.tempe.gov/datasets/0c333bd164d64d62aa0ee6f99b1ccf82_0/explore
  - Model Information & Packages: https://catboost.ai

- Where to send questions or comments about the model: 
  - noahruiz416@gmail.com

## Intended use

_Use cases that were envisioned during development._

Review section 4.2 of the [model cards paper](https://arxiv.org/abs/1810.03993).

### Primary intended uses
- Understand features which increase the likelihood of fatal traffic accidents in the City of Tempe 
- Gain a better understanding of fatal traffic accidents in the City of Tempe
- Shed of light on areas of improvement for the City of Tempe's vision zero goal

### Primary intended users
- Maricopa County Officials 
- City of Tempe Policy Makers

### Out-of-scope use cases
- Trying to predict if a person will get into a fatal accident or not (model lacks high precision)

## Factors

### Relevant factors
-

## Evalutation Metrics
- Recall 
- Precision 
- F1 Score 
- AUC

### Model performance measures
- The following metrics are standard for classification problems and each evaluate a certain aspect of classification performance 
- In particular Recall was the primary metric for this project, as we wanted a model that was able to maintain a high level of true positives regardless of prediction quality 
- Precision was not as important given the imbalanced nature of this problem
- Because of this our model has an inherent trade-off between precision and recall. 
- In this case we chose to build a model that maximizes Recall at the cost of Precision

### Approaches to uncertainty and variability
- Due to the imbalanced nature 

## Training Data
- Several features were created from the initial dataframe 
- We broke up datetime into various categories in order to add a time element into our feature vector 
- Additionally to reduce dimensionality we create a 'median age' column which captures the median age between the two drivers involved in the accident 
- Further various binary columns were created to measure if drugs, alchol, pedestrians or cyclists were involved in the accident 
- Finally we randomly undersampled the majority class to solve the imbalance problem


### Datasets
- 'https://data.tempe.gov/datasets/0c333bd164d64d62aa0ee6f99b1ccf82_0/explore?location=33.389151%2C-111.927944%2C12.80'

### Motivation
- Understand underlying features behind a fatal traffic accident

### Preprocessing
- Dropped N/A values, led to some data loss
- However before dropping N/A values, the distirbution of classes was checked and by dropping N/A values the underlying shape of the dataset remained the same  


## Quantitative analyses

### Unitary results:
- Catboost Classiifcation Model trained with undersampled data
- Our final implementation using Catboost Classification recieved the following scores based on our evaluation metrics: 
  - Recall:
  - Precision: 
  - F1 Score:
  - Accuracy:
  - AUC:

- Further we conduct cross validation in order to gain a generalized understanding of model performance

## Ethical considerations

### Data
- 

### Risks and harms
- 

## Caveats and recommendations
- 

