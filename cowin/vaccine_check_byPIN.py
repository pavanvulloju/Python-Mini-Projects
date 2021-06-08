import requests
from datetime import datetime, timedelta

today = datetime.today()

day_var = 7
this_week_dates = []
for day in range(day_var):
	this_week_dates.append((today + timedelta(day)).strftime("%d-%m-%y"))


def check_by_pin(pin):
	print(f'Here is your required data for {pin} pincode: \n'+'--'*30)

	for date in this_week_dates:
		result = requests.get(f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={pin}&date={date}')
		json_data = result.json()
		print(f'On {date} day')
		if json_data['centers']:
			for center in json_data['centers']:
				for session in center['sessions']:
					print("Center Name :", center['name'])
					print("Address :", center['address'])
					print("date: ", date)
					print("age_limit: ", session['min_age_limit'])
					print("vaccine:", session['vaccine'])
					print("fee: ",center['fee_type'])
					print("--" * 30)

		else:
			print('Data Not available')
			print("--" * 30)


if __name__ == '__main__':
	pincode = input("Enter Pincode and get the data from CoWIN website: ")
	check_by_pin(pincode)