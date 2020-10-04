from flask import Flask, request, render_template
import sklearn
import pickle
import pandas as pd
import numpy as np 

app = Flask(__name__)
model = pickle.load(open("flight_xgb.pkl", "rb"))

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict", methods = ["GET", "POST"])
def predict():
    if request.method == "POST":

        # Date_of_Journey
        date_dep = request.form["Dep_Time"]
        Journey_day = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
        Journey_month = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").month)
        # print("Journey Date : ",Journey_day, Journey_month)

        # Departure
        Dep_hour = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").hour)
        Dep_min = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").minute)
        # print("Departure : ",Dep_hour, Dep_min)

        # Arrival
        date_arr = request.form["Arrival_Time"]
        Arrival_hour = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").hour)
        Arrival_min = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").minute)
        # print("Arrival : ", Arrival_hour, Arrival_min)

        # Duration
        if Dep_hour>Arrival_hour:
        
            hours = Arrival_hour + 24 - Dep_hour
        
        else:
            hours = Arrival_hour - Dep_hour

        minutes = Arrival_min - Dep_min
 
        Duration = hours * 60 + minutes
        # print("Duration : ", dur_hour, dur_min)

        # Total Stops
        Total_stops = int(request.form["stops"])
        # print(Total_stops)

        # Airline
        # AIR ASIA = 0 (not in column)
        airline=request.form['airline']
        if(airline=='Air Asia'):
            AirIndia = 0
            GoAir = 0
            IndiGo = 0
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 0
            SpiceJet = 0
            Trujet = 0
            Vistara = 0
            Vistara_Premium_economy = 0
             

        elif (airline=='Air India'):
            AirIndia = 1
            GoAir = 0
            IndiGo = 0
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 0
            SpiceJet = 0
            Trujet = 0
            Vistara = 0
            Vistara_Premium_economy = 0

        elif (airline=='GoAir'):
            AirIndia = 0
            GoAir = 1
            IndiGo = 0
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 0
            SpiceJet = 0
            Trujet = 0
            Vistara = 0
            Vistara_Premium_economy = 0 
            
        elif (airline=='IndiGo'):
            AirIndia = 0
            GoAir = 0
            IndiGo = 1
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 0
            SpiceJet = 0
            Trujet = 0
            Vistara = 0
            Vistara_Premium_economy = 0
            
        elif (airline=='Multiple Carriers'):
            AirIndia = 0
            GoAir = 0
            IndiGo = 0
            Multiple_carriers = 1
            Multiple_carriers_Premium_economy = 0
            SpiceJet = 0
            Trujet = 0
            Vistara = 0
            Vistara_Premium_economy = 0
            
        elif (airline=='Multiple Carriers Premium Economy'):
            AirIndia = 0
            GoAir = 0
            IndiGo = 0
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 1
            SpiceJet = 0
            Trujet = 0
            Vistara = 0
            Vistara_Premium_economy = 0

        elif (airline=='SpiceJet'):
            AirIndia = 0
            GoAir = 0
            IndiGo = 0
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 0
            SpiceJet = 1
            Trujet = 0
            Vistara = 0
            Vistara_Premium_economy = 0

        elif (airline=='Trujet'):
            AirIndia = 0
            GoAir = 0
            IndiGo = 0
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 0
            SpiceJet = 0
            Trujet = 1
            Vistara = 0
            Vistara_Premium_economy = 0

        elif (airline=='Vistara'):
            AirIndia = 0
            GoAir = 0
            IndiGo = 0
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 0
            SpiceJet = 0
            Trujet = 0
            Vistara = 1
            Vistara_Premium_economy = 0

        else:
            AirIndia = 0
            GoAir = 0
            IndiGo = 0
            Multiple_carriers = 0
            Multiple_carriers_Premium_economy = 0
            SpiceJet = 0
            Trujet = 0
            Vistara = 0
            Vistara_Premium_economy = 1

        Source = request.form["Source"]
        if (Source == 'Delhi'):
            s_Chennai = 0
            s_Delhi = 1
            s_Kolkata = 0
            s_Mumbai = 0
            

        elif (Source == 'Kolkata'):
            s_Chennai = 0
            s_Delhi = 0
            s_Kolkata = 1
            s_Mumbai = 0
           

        elif (Source == 'Mumbai'):
            s_Chennai = 0
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 1
            

        elif (Source == 'Chennai'):
            s_Chennai = 1
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 0
            

        else:
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 0
            
        # Destination
        # Banglore = 0 (not in column)
        Destination = request.form["Destination"]
        if (Destination == 'Cochin'):
            d_Cochin = 1
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0
        
        elif (Destination == 'Delhi'):
            d_Cochin = 0
            d_Delhi = 1
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0

        elif (Destination == 'New Delhi'):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 1
            d_Hyderabad = 0
            d_Kolkata = 0

        elif (Destination == 'Hyderabad'):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 1
            d_Kolkata = 0

        elif (Destination == 'Kolkata'):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 1

        else:
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0

        test = np.array([[
            Duration,
            Total_stops,
            Dep_hour,
            Dep_min,
            Arrival_hour,
            Arrival_min,
            Journey_day,
            Journey_month,
            AirIndia,
            GoAir,
            IndiGo,
            Multiple_carriers,
            Multiple_carriers_Premium_economy,
            SpiceJet,
            Trujet,
            Vistara,
            Vistara_Premium_economy,
            s_Chennai,
            s_Delhi,
            s_Kolkata,
            s_Mumbai,
            d_Cochin,
            d_Delhi,
            d_Hyderabad,
            d_Kolkata,
            d_New_Delhi
        ]])


        prediction=model.predict(test)

        
        print(prediction)
        
        output= np.round(prediction[0],decimals = 0)

        return render_template('home.html',prediction_text="Your flight price is Rs. {}".format(output))


    return render_template("home.html")



if __name__ == "__main__":
    app.run(debug=True)
