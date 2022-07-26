#This script takes in the cleaned tempe traffic data file and outputs a feature engineered dataset that is prepared for final modeling
#dependent on pandas and python 3.9 and the ETL Script

import pandas as pd

cleaned_data = pd.read_csv("/users/n/Tempe_Traffic_V.2/no_null_vals_df.csv")

#function to binary encode accidents as fatal or nonfatal
#by appending a zero or one to the severity column we essentially are able to create a binary label that will serve as our target variable
def encode_fatal_accidents(data):
  Severity = []
  for row in data['Injuryseverity']:
    if row != "Fatal":
      Severity.append(0) #nonfatal
    if row == "Fatal":
      Severity.append(1) #fatal
  data['Fatal_Non_Fatal'] = Severity

#finds columns that will not add anything as a feature and simply drops said columns
def drop_useless_cols(data):
  return_data = data.drop(labels = ['X', 'Y',
                      'Incidentid', 'Year',
                       'Latitude', 'Longitude',
                       'Totalfatalities', 'Distance', 'OBJECTID', 'Age_Drv1', 'Age_Drv2', 'Gender_Drv1', 'Gender_Drv2', 'Injuryseverity'], axis = 1)
  return return_data

#helper function that contains the logic for whether or not drugs were involved in an accident
def label_drugs(row):
  if row['DrugUse_Drv1'] == "Drugs" or row['DrugUse_Drv2'] == "Drugs":
    return 1 #drugs are involved
  if row['DrugUse_Drv1'] != "Drugs" or row['DrugUse_Drv2'] != "Drugs":
    return 0 #drugs are not involved

#helper function that contains the logic for whether or not alch was involved in an accident
def label_alchol(row):
  if row['AlcoholUse_Drv1'] == "Alcohol" or row['AlcoholUse_Drv2'] == "Alcohol":
    return 1 #drugs are involved
  if row['AlcoholUse_Drv1'] != "Alcohol" or row['AlcoholUse_Drv2'] != "Alcohol":
    return 0 #drugs are not involved

#function to call helper functions and implement drugs / alch invovled logic
def apply_drug_alchol_label(input_data):
  data1 = input_data['drugs_involved'] = input_data.apply (lambda row: label_drugs(row), axis=1)
  data1 = input_data['alcohol_involved'] = input_data.apply (lambda row: label_alchol(row), axis=1)

#helper function to label whther or not a car was involed in an accident
def label_car(row):
  if row['Unittype_One'] == "Driver" or row['Unittype_Two'] == "Driver":
    return 1 #car was involved
  if row['Unittype_One'] != "Driver" or row['Unittype_Two'] != "Driver":
    return 0 #car was not involved

def label_cyclist(row):
  if row['Unittype_One'] == "Pedalcyclist" or row['Unittype_Two'] == "Pedalcyclist":
    return 1 #bike was involved
  if row['Unittype_One'] != "Pedalcyclist" or row['Unittype_Two'] != "Pedalcyclist":
    return 0 #bike was not involved

def label_pedestrian(row):
  if row['Unittype_One'] == "Pedestrian" or row['Unittype_Two'] == "Pedestrian":
    return 1 #Pedestrian was involved
  if row['Unittype_One'] != "Pedestrian" or row['Unittype_Two'] != "Pedestrian":
    return 0 #Pedestrian was not involved

def label_driverless(row):
  if row['Unittype_One'] == "Driverless" or row['Unittype_Two'] == "Driverless":
    return 1 #no driver was involved
  if row['Unittype_One'] != "Driverless" or row['Unittype_Two'] != "Driverless":
    return 0 #no driver was involed

#applying the above functions in one nice format
def apply_unit_type_labels(input_data):
  data1 = input_data['Car_Involved'] = input_data.apply (lambda row: label_car(row), axis=1)
  data1 = input_data['Pedalcyclist_Involved'] = input_data.apply (lambda row: label_cyclist(row), axis=1)
  data1 = input_data['Pedestrian_Involved'] = input_data.apply (lambda row: label_pedestrian(row), axis=1)
  data1 = input_data['Driverless'] = input_data.apply (lambda row: label_driverless(row), axis=1)


#this function drops bad columns in light conditions, violations and collisionmanner
def drop_useless_rows(input_data):
  data1 = input_data[input_data['Lightcondition'].str.contains("51")==False]
  data2 = data1[data1['Lightcondition'].str.contains("Unknown 51")==False]
  data3 = data2[data2['Violation1_Drv1'].str.contains("108")==False]
  data4 = data3[data3['Violation1_Drv1'].str.contains("109")==False]
  data5 = data4[data4['Violation1_Drv1'].str.contains("49")==False]
  data6 = data5[data5['Collisionmanner'].str.contains("10")==False]
  return data6

#this function removes outlier driving ages in the data_set and then calculates the median age between the two drivers and creates a new column
def age_manipulation(input_data):
  data = input_data.drop(input_data.index[input_data['Age_Drv1'] >= 100], inplace=False)
  data1 = data.drop(data.index[data['Age_Drv2'] >= 100], inplace=False)
  data1['median_age'] = (data1['Age_Drv1'] + data1['Age_Drv2']) / 2
  return data1

#function to call all the cleaning methods at once
def clean_dataset(input_data):
  input_data_rows_dropped = drop_useless_rows(input_data)
  age_manipulated_data = age_manipulation(input_data_rows_dropped)
  return age_manipulated_data

#drops additional columns, use after calling the age manipulation function
def drop_more_cols(data):
  return_data = data.drop(labels = ['AlcoholUse_Drv1', 'AlcoholUse_Drv2', 'DrugUse_Drv1', 'DrugUse_Drv2'], axis = 1)
  return return_data

#main function to call and apply above functions
def main():
    df = pd.read_csv("/users/n/Tempe_Traffic_V.2/no_null_vals_df.csv")

    #the encode function simply creates our binary labels for fatal or non fatal accidents
    encode_fatal_accidents(df)

    #setting our clean dataset equal to our cleaned and encoded dataframe
    clean_dat = clean_dataset(df)

    #dropping useless cols within the clean dataset
    clean_dat2_all = drop_useless_cols(clean_dat)

    #applying drug and alchol labels
    apply_unit_type_labels(clean_dat2_all)
    apply_drug_alchol_label(clean_dat2_all)

    #dropping more cols
    clean_dat2_all = drop_more_cols(clean_dat2_all)

    # define bins and labels for time analysis
    bins = ['00:00:00', '01:00:00' ,'06:00:00', '11:00:00', '17:00:00', '23:00:00', '23:59:59']
    labels = ['Night', 'Early Morning','Morning', 'Noon', 'Evening','Night']

    # convert to timedelta
    s = pd.to_timedelta(pd.to_datetime(clean_dat2_all['DateTime']).dt.time.astype(str))
    clean_dat2_all['time_analysis'] = pd.cut(s, bins=pd.to_timedelta(bins), labels=labels, ordered=False)
    clean_dat2_all.dropna(inplace = True)

    #having our initial input vector of all values into one dataframe
    input_vector = clean_dat2_all.drop(labels = ['Fatal_Non_Fatal', 'Totalinjuries', 'DateTime', 'Unittype_One', 'Unittype_Two'], axis = 1)


    #we then load the data into to different dataframes one with our input vector and the other with train/test labels
    X = input_vector
    y = clean_dat2_all['Fatal_Non_Fatal']

    #final tweaks to get data into proper format for analysis
    X['time_analysis'] = X['time_analysis'].astype('object')
    X['drugs_involved'] = X['drugs_involved'].astype('int')
    X['alcohol_involved'] = X['alcohol_involved'].astype('int')

    #with our X input dataframe and our y target labels specified we can now load our inputs and labels into dataframes for modeling
    X.to_csv("X_input_data.csv", index=False)
    y.to_csv("y_label_data.csv", index=False)

#call this method to trigger the following script
main()
