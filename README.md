# Flight Price Prediction
Dataset link: https://www.kaggle.com/nikhilmittal/flight-fare-prediction-mh

In this project I have built a model which predicts flight price by taking few inputs such as departure date, arrival date, airline, source and destination. \
Link to web application: https://flight-prices-prediction.herokuapp.com/

<img width="379" alt="Screenshot 2020-10-07 214447" src="https://user-images.githubusercontent.com/48923446/95358201-6b433900-08e6-11eb-9a6d-4a1c14b6a058.png">

# Model Building
I have dropped Jet airways airlines because it is shutdown now. There is no point in training on that data.

Before dropping Jet Airways I cheched built few models just to compare them with models built after dropping Jet airways.

Here are the observed results for r squared metric.

<img width="253" alt="JET AIR " src="https://user-images.githubusercontent.com/48923446/95361296-2faa6e00-08ea-11eb-827d-b1c37e6a6156.png">

Results after dropping Jet airways from airline column:

<img width="353" alt="metrics_flight" src="https://user-images.githubusercontent.com/48923446/95487143-8dee5400-09b1-11eb-9ae3-4c67fb52239f.png">


I have selected XGB without tuning as my final model.

Here is the plot for feature importances. Total stops is the most important feature in predicting the flight prices.

<img width="668" alt="flightprice_feature_importances" src="https://user-images.githubusercontent.com/48923446/95487102-829b2880-09b1-11eb-915d-4ebe6131465d.png">

The scatter plot for y_true and y_prediction.

<img width="654" alt="y_y_p_flight" src="https://user-images.githubusercontent.com/48923446/95487264-bb3b0200-09b1-11eb-9aa9-6cbea850dfda.png">

Below plot shows that there is normality in residuals.

<img width="653" alt="resid_flight" src="https://user-images.githubusercontent.com/48923446/95487120-875fdc80-09b1-11eb-9d56-08a18ff4e59a.png">
