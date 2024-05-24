import streamlit as st
import datetime
import requests


'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
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




# params = {"pickup_datetime": pickup_datetime,
#                  "pickup_longitude": pickup_longitude,
#                  "pickup_latitude": pickup_longitude,
#                  "dropoff_longitude": dropoff_longitude,
#                  "dropoff_latitude": dropoff_latitude,
#                  "passenger_count": passenger_count}


# test_params = {
#     "pickup_datetime": '2013-07-06 10:18:00',
#     "pickup_longitude": '-73.70',
#     "pickup_latitude": '40.9',
#     "dropoff_longitude": '-73.98',
#     "dropoff_latitude": '40.70',
#     "passenger_count": '2'}

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

# if params != None:
# url = 'https://taxifare.lewagon.ai/predict'
# response = requests.get(url, params)
# tmp = response.json()
# # price = tmp['fare']
# st.write(response.status_code)



# import streamlit as st
# import datetime
# from datetime import datetime, date, time
# import requests

# # page configuration
# st.set_page_config(page_title="Taxi Fare Predictor", page_icon="🚖", layout="centered")

# #title and subtitle
# st.title("Taxi Fare Predictor 🚖")
# st.markdown("### Predict the fare of your taxi ride in New York City")

# #my code:
# with st.form('Insert the following parameters'):
#     pickup_dt = st.date_input("Select a date")
#     pickup_tm= st.time_input("Select a time")
#     datetime_value = datetime.combine(pickup_dt,pickup_tm)
#     #datetime_value = st.text_input("date and time",'2013-07-06 17:18:00')
#     pickup_lon= st.text_input("pickup longitude", '-73.950655')
#     pickup_lat= st.text_input("pickup latitude", '40.783282')
#     dropoff_lon= st.text_input("dropoff longitude", '-73.984365')
#     dropoff_lat= st.text_input("dropoff latitude", '40.769802')
#     num_passengers = st.selectbox("Number of passengers", list(range(1, 11)))

#     submitted = st.form_submit_button("Submit")
#     if submitted:
#         query = {
#             'pickup_datetime':datetime_value,
#             'pickup_longitude':float(pickup_lon),
#             'pickup_latitude': float(pickup_lat),
#             'dropoff_longitude':float(dropoff_lon),
#             'dropoff_latitude': float(dropoff_lat),
#             'passenger_count': int(num_passengers)
#         }

# query= {"pickup_datetime":datetime_value, "pickup_longitude":float(pickup_lon), "pickup_latitude":float(pickup_lat),
#         "dropoff_longitude":float(dropoff_lon)  , "dropoff_latitude":float(dropoff_lat), "passenger_count":int(num_passengers)
#        }

# url = 'https://taxifare.lewagon.ai/predict'
# response= requests.get(url=url, params=query).json()
# fare= response["fare"]

# st.write(fare)

# # Add footer
# st.markdown("""
#     <style>
#     .footer {
#         position: fixed;
#         left: 0;
#         bottom: 0;
#         width: 100%;
#         background-color: rgba(232, 234, 235, 0.8);
#         text-align: center;
#         padding: 10px;
#         font-size: 14px;
#         color: #333;
#     }
#     </style>
#     <div class="footer">
#         Created with ❤️ by Max
#     </div>
#     """, unsafe_allow_html=True)
