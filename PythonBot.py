from ppadb.client import Client
from datetime import datetime
import pytz
import time 

def validate(date_text):
    try:
        if date_text != datetime.strptime(date_text, "%H:%M:%S").strftime("%H:%M:%S"):
            raise ValueError
        return True
    except ValueError:
        return False

def check_is_digit(input_str):
    if 0< input_str <=6:
        return True
    else:
        return False

adb = Client(host='127.0.0.1', port=5037)
devices = adb.devices()

if len(devices) == 0:
    print('no device attached')
    quit()

device = devices[0]

time_confirmation= 1
while (time_confirmation==1):
    selected_date = input("\nWhat time do you wish to book the court at\n")

    if validate(selected_date) == 1:
        print("\nTime accepted, bot sequence commencing\n")
        time_confirmation = 0
    else:
        print("\nWrong time format, try again (H:M:S)\n")

time.sleep(1)
block_confirmation = 1

while (block_confirmation==1):
    block_chosen = int(input("\nWhat block shall we select today\n"))
    if check_is_digit(block_chosen) == 1:
        print("\nBlock Selected\n")
        block_confirmation = 0
    else:
        print("\nWrong Block format, try again (A # between 1 to 6)\n")

time.sleep(1)
print("\3:0nOperation Kill Court Hoarders Has begun \n")

val = 1
val2 = 0
while (val==1) : 
    tz_UAE = pytz.timezone('Asia/Kolkata') 
    datetime_UAE = datetime.now(tz_UAE)
    string_datetime_UAE = datetime_UAE.strftime("%H:%M:%S")
    if string_datetime_UAE == selected_date:
        val = 0
        print("\ntime to book a court \n")
        if block_chosen==1:
            device.shell('input touchscreen swipe 600 280 600 280 2')
            val2 = 1
        elif block_chosen==2:
            device.shell('input touchscreen swipe 600 460 600 460 1')
            val2 = 1
        elif block_chosen==3:
            device.shell('input touchscreen swipe 600 640 600 640 1')
            val2 = 1
        elif block_chosen==4:
            device.shell('input touchscreen swipe 600 810 600 810 1')
            val2 = 1
        elif block_chosen==5:
            device.shell('input touchscreen swipe 600 980 600 980 1')
            val2 = 1
        elif block_chosen==6:
            device.shell('input touchscreen swipe 600 1160 600 1160 1')
            val2 = 1

if val2 == 1: 
    time.sleep(5)
    device.shell('input touchscreen swipe 600 640 600 640 1')
    print('\nBooking Has succesfully commenced, congrats comrade\n') 

# A bot by Avya Malhora
