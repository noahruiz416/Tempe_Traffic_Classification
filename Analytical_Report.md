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
