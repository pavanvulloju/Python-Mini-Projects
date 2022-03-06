from datetime import datetime
import csv
import psutil
import time

START_BATTERY_POINT = 5
END_BATTERY_POINT = 99  # 99 For Full Script
SCRIPT_START = datetime.now().timestamp()


def get_time():
	battery = psutil.sensors_battery()
	next_point = battery.percent + 1
	start = datetime.now().timestamp()
	while True:
		battery_status_new = psutil.sensors_battery().percent
		if battery_status_new == next_point:
			break
		time.sleep(2)
	end = datetime.now().timestamp()
	return end-start


with open('data.csv', 'w', newline='') as file:
	writer = csv.writer(file)
	for a in range(START_BATTERY_POINT, END_BATTERY_POINT+1):
		battery_status = psutil.sensors_battery()
		if battery_status.power_plugged:
			if a == battery_status.percent:
				value = get_time()
				writer.writerow([str(a)+'->'+str(a+1), int(value)])
				print(str(a) + ' -> ' + str(a + 1) + f" secs: {int(value)}")
		else:
			print("You might want to plug in the PC")
			break


SCRIPT_END = datetime.now().timestamp()

print("Total time taken is: " + str(SCRIPT_END-SCRIPT_START) + " secs")
print('Script Run Completed !!!')
