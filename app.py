import streamlit as st
import datetime
import requests


'''
# TaxiFareModel front
'''



# params = None

with st.form('Insert the following Parameters'):
    pickup_date = st.date_input("Pickup Date")
    pickup_time = st.time_input('Pickup Time')
    pickup_datetime = f'{pickup_date} {pickup_time}'
    pickup_longitude = st.number_input("Pickup Longitude")
    pickup_latitude = st.number_input("Pickup Latitude")
    dropoff_longitude = st.number_input("Dropoff Longitude")
    dropoff_latitude = st.number_input("Dropoff Latitude")
    passenger_count = st.text_input("Passenger Count")
    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        params = {"pickup_datetime": pickup_datetime,
                 "pickup_longitude": pickup_longitude,
                 "pickup_latitude": pickup_latitude,
                 "dropoff_longitude": dropoff_longitude,
                 "dropoff_latitude": dropoff_latitude,
                 "passenger_count": passenger_count}
        url = 'https://taxifare.lewagon.ai/predict'
        response = requests.get(url, params)
        tmp = response.json()
        price = tmp['fare']
        st.write(price)


