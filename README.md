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

<img width="216" alt="rm jet air" src="https://user-images.githubusercontent.com/48923446/95361005-cb87aa00-08e9-11eb-9e66-a7fab00d11a4.png">
