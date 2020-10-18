# Flight Price Prediction

![flight](https://user-images.githubusercontent.com/48923446/95487431-f3424500-09b1-11eb-8e18-9a2394fa5acd.jpg)


In this project I have built a model which predicts flight price by taking few inputs such as departure date, arrival date, airline, source and destination. \
Link to web application: https://flight-prices-prediction.herokuapp.com/


Dataset link: https://www.kaggle.com/nikhilmittal/flight-fare-prediction-mh

# Data Description
The dataset consists of 11 features 
Airline  :- Name of airline iin which passenger is travelling
Date_of_Journey:- Date of journey in year, month and date format. 
Source:- City from which passenger is travelling.
Destination:- City to which passenger is travelling.
Route:- Route which aeroplane takes. It includes all the stoppages.
Dep_Time:- Time at which aeroplane departs.
Arrival_Time:- Time at which aeroplane reaches destination.
Duration:- Duration of entire journey.
Total_Stops:- Total stops of aeroplane during the journey
Additional_Info:- Additional information such as meals included etc.
Price:- Price of the ticket which is the target feature.

# Preprocessing
Dropped  route and additional info columns.
Departure time and Arrival time are strings. We need to extract hour and minute from both the columns.
Extracted journey date, journey month and journey day(day of the week) from Date_of_Journey column and dropped that column after extracting.
Created a new duration column. Even tough duration column is available, it is a string. Extracted hour and minutes from the string and converted it into minutes. Now all the duration values are in minutes. Used joblib for this task for parallel processing.
One hot encoded all the categorical features as all of them are nominal. Now the dataset is ready to be modelled.

# Model Building
I have dropped Jet airways airlines because it is shutdown now. There is no point in training on that data.

Before dropping Jet Airways I cheched built few models just to compare them with models built after dropping Jet airways.

Here are the observed results for r squared metric.

<img width="253" alt="JET AIR " src="https://user-images.githubusercontent.com/48923446/95361296-2faa6e00-08ea-11eb-827d-b1c37e6a6156.png">

Results after dropping Jet airways from airline column:

<img width="353" alt="metrics_flight" src="https://user-images.githubusercontent.com/48923446/95487143-8dee5400-09b1-11eb-9ae3-4c67fb52239f.png">


I have selected XGB with tuning as my final model.

Here is the plot for feature importances. Total stops is the most important feature in predicting the flight prices.

<img width="668" alt="flightprice_feature_importances" src="https://user-images.githubusercontent.com/48923446/95487102-829b2880-09b1-11eb-915d-4ebe6131465d.png">

The scatter plot for y_true and y_prediction.

<img width="654" alt="y_y_p_flight" src="https://user-images.githubusercontent.com/48923446/95487264-bb3b0200-09b1-11eb-9aa9-6cbea850dfda.png">

Below plot shows that there is normality in residuals.

<img width="653" alt="resid_flight" src="https://user-images.githubusercontent.com/48923446/95487120-875fdc80-09b1-11eb-9d56-08a18ff4e59a.png">
