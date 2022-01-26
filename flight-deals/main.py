# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes
# to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = "LON"

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

flight_search = FlightSearch()
notification_manager = NotificationManager()

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(f"sheet_data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_date=tomorrow,
        to_date=six_month_from_today
    )
    try:
        flight.price < destination["lowestPrice"]
    except BaseException:
        notification_manager.send_sms("No flight available at the time.")
    else:
        notification_manager.send_sms(
            message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} "
                    f"to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} "
                    f"to {flight.return_date}."
        )