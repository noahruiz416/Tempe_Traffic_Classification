# Project Summary 

In the United States fatal car accidents and traffic accidents at large continue to be an ongoing problem for commuters, policy makers and urban planners. 
In 2020 the NSC estimated that the average fatal car accident can lead to an economic cost of 1.7 million dollars. 
Additionally, the NSC found that even accidents where no injury was observed could lead to an average of $12,800 of economic cost per accident. 
These figures above show the potential economic damages that traffic accidents both fatal and minor can cause. Because of this many municipalities across the nation have begun initiatives to reduce the number of fatal accidents that occur within their area of influence. 
One specific program that affects many university students and citizens within Maricopa County is the City of Tempe’s “Vision Zero” which aims at drastically reducing fatal traffic accidents within the City of Tempe.

Vision Zero has led to the City of Tempe releasing a large amount of accident data reports to the public which can be accessed by anyone with computer access.
While analyzing the progress of “Vision Zero” I found the existing reports to be very clunky and additionally the dashboards and visualization were slow to load and use. 
Additionally, while reading the reports, I began to wonder if a model can be created to classify fatal traffic accidents and gain an understanding of features that may lead to a fatal accident. 
This led to the following project being undertaken with the goal of improving our understanding of fatal traffic accidents within the City of Tempe.

From the use of CAT Boost Classification, I was able to find that it is possible to classify fatal and nonfatal accidents. 
However, the model is not perfect and lacks from a very low amount of precision, leading to many false positive (false fatal) classifications.
Despite this though our model when cross validated and tested with out of sample data receives a very high recall rate of around 0.80 – 0.90 on average. 
In short this shows that our model can identify fatal car accidents with good accuracy however it tends to overestimate the number of fatal car accidents and ends up classifying a large amount of non-fatal accidents as fatal. 

Because of this I would not recommend using this model for pure classification, due to the large number of false positives.
Further the exploratory analysis conducted reveals the severe imbalance between fatal and nonfatal accidents which most causes the classification model to suffer in quality. 
An important takeaway from this analysis is that although we may not be able to predict fatal traffic accidents with both high precision and recall, it is still possible to use our model to highlight features which lead to fatal accidents. 

# Model Visualizations

## Feature Importance on Train Data
<img width="500" alt="Screen Shot 2022-07-26 at 7 08 06 AM" src="https://user-images.githubusercontent.com/88412646/181068119-d460812f-6818-490b-9a5b-25067b6fdd52.png">

## Feature Importance on Test Data
<img width="500" alt="Screen Shot 2022-07-26 at 7 08 28 AM" src="https://user-images.githubusercontent.com/88412646/181068197-5816764c-9ef3-46b3-91c9-78c3d85d8b6f.png">

This chart shows the weight of various features on classifying fatal or non-fatal traffic accidents. From the graph it is clear that there are several features that have very strong importance in classifying our accidents. In particular we find that the commonly held notion of time, drugs, alchol and age all being key indicators of a fatal traffic accident to hold true. Our model reports that the time of day and whether or not alchol or drugs were involved tend to be the strongest contributors of classifications.

Regarding the Shap Value it is simply a measure of how "much" a feature contributes to our classifications. A higher shap value indicates that the feature contributes a great deal to classifications while a small follow the opposite.

Interstingly enough the cross street, street name and collission manner have little relevance in classifying fatal accidents which is quite suprising. Further the train and test data have the same levels of feature importance.

## Confusion Matrix on Test Data
<img width="500" alt="Screen Shot 2022-07-26 at 7 08 51 AM" src="https://user-images.githubusercontent.com/88412646/181068277-1cfca768-1e21-4692-8462-ed2e3ddb7c9e.png">

The confusion matrix shows the quality of our predictions. On the upper left and lower right cells we see the predictions that were correct or the true positives and true negatives. On the upper right and lower left cells we can see the false positives and the false negatives. As you can see we have a very high amount of false positives which indicates that our model is not precise and makes poor quality decisions regarding the "fatal" classification. However I content with the models ability to classify true positives correctly. As you can see the model predicted 16 true positives, which indicates that our model is able to properly classify fatal accidents. 

Given the nature of the imbalanced data and rarity of a fatal car accident, it is clear that there will be a tradeoff between precision and recall or in other terms, a tradeoff between the quality and quantity of true positive predictions. In this case I believe that despite the tradeoff, it is worthwhile to make since we gain an understanding of features that may affect a positive classification.

## ROC Curve on Test Data
<img width="500" alt="Screen Shot 2022-07-26 at 7 09 19 AM" src="https://user-images.githubusercontent.com/88412646/181068368-3f643e7f-5867-4b1a-a6f8-7ecd4ac23250.png">

The ROC Curve shows the tradeoff between the False Positive Rate and the True Positive Rate at various probability thresholds. Since we are dealing with an imbalanced data problem the ROC Curve is not as important. In particular the ROC Curve tends to be overly optimistic on the imbalanced data. For this reason we will not focus on this metric.
