# Tempe Traffic Classification Project Directory
Traffic Classification Model with the Goal of understanding fatal accidents in the City of Tempe through the use of Machine Learning & Statistics. In particular various classification algorithims will be used in order to classify accidents based on whether or not a fatality occured in a given accident. Additionally extensive analysis will be conducted in this project to give Tempe policy makers a better understanding of the progress of the "vision zero" mission.

Quick Summary:
- We find that "median age between drivers", "drug use", "alchol use" and "time category" were key features in classifying an accident as fatal or nonfatal 
- Further we find that a severe imbalance exists within classes, with less than 1% of accidents being fatal 
- Fatalaties have decreased throughout the years, showing "Vision Zero" is going towards the right direction 
- Southern Ave, Baseline Rd, Broadway Rd, University Rd and Scottsdale Rd are the top 5 most frequent fatal streets in the City of Tempe with 4 out of those five also being the most frequent non-fatal accident streets as well
- Our model presents high recall (0.90) a the cost of very low precision (>0.05)

## Resource Guide:
Within this readme you will find various links, which lead to different files in this repository. 

### Analytical Report 
Provides a analysis of the key takeaways and findings of this project and potential next steps + recommendations:
- https://github.com/noahruiz416/Tempe_Traffic_Classification/edit/main/Analytical_Report.md

### Model Card 
Provides a brief overview of the project and various metrics, models and ethical considerations when putting the project together:
- https://github.com/noahruiz416/Tempe_Traffic_Classification/blob/main/Model_Card.md

### Deliverable Files 
Production files for the model:
- Dependencies: Python 3.9+, Numpy, Pandas, Sklearn, Seaborn, Matplotlib, Catboost, Imblearn

### Prototype
Initial Exploratory Notebook Analysis of the dataset itself, treat as a draft and not the final product of this analysis:
- https://github.com/noahruiz416/Tempe_Traffic_Classification/tree/main/Prototypes

### Data:
Dataset used for this analysis, the dataset caputures service usage for traffic accidents  in Maricopa County from January 2012 - December 2020:
- https://github.com/noahruiz416/Tempe_Traffic_Classification/tree/main/Data

### Data Dictionary:
Description of each of the fields in the dataset, good place to start for understanding the project. This link will send you to another site that contains the data dictionary:
- https://gis.tempe.gov/design/data-dictionary/1.08%20Crash%20Data%20(detail)/
