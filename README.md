# Flight Price Prediction
Dataset link: https://www.kaggle.com/nikhilmittal/flight-fare-prediction-mh

In this project I have built a model which predicts flight price by taking few inputs such as departure date, arrival date, airline, source and destination. \
I have deployed the model using flask, you can access it from this link https://flight-prices-prediction.herokuapp.com/

<img width="379" alt="Screenshot 2020-10-07 214447" src="https://user-images.githubusercontent.com/48923446/95358201-6b433900-08e6-11eb-9a6d-4a1c14b6a058.png">

# Model Building
I have dropped Jet airways airlines because it is shutdown now. There is no point in training on that data.

Before dropping Jet Airways I cheched built few models just to compare them with models built after dropping Jet airways.

Here are the observed results for r squared metric.

<img width="253" alt="JET AIR " src="https://user-images.githubusercontent.com/48923446/95361296-2faa6e00-08ea-11eb-827d-b1c37e6a6156.png">

Results after dropping Jet airways from airline column:

<img width="242" alt="rm jet air " src="https://user-images.githubusercontent.com/48923446/95361783-cd05a200-08ea-11eb-8c31-eb97d8853ec9.png">


I have selected XGB without tuning as my final model.

Here is the plot for feature importances

<img width="501" alt="flightprice_feature_importances" src="https://user-images.githubusercontent.com/48923446/95364239-363ae480-08ee-11eb-831b-bf4b792c1dd4.png">

The scatter plot for y_true and y_prediction.

<img width="284" alt="t_p_scat" src="https://user-images.githubusercontent.com/48923446/95364354-5bc7ee00-08ee-11eb-8b51-ca1613e88cba.png">

Below plot shows that there is Normality of residuals

<img width="268" alt="resid_hist" src="https://user-images.githubusercontent.com/48923446/95364375-608ca200-08ee-11eb-9107-8ae0de9c8f4e.png">
