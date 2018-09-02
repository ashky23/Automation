import time
import webbrowser as wb
set_alarm = input("Set the Website alarm as H:M:S:")
url = input("Enter the website you want to open:")
Actual_time = time.strftime("%I:%M:%S")
print(Actual_time)
while (set_alarm != Actual_time):
    #print("The time is "+ Actual_time)
    Actual_time = time.strftime("%I:%M:%S")
    time.sleep(1)
if (Actual_time == set_alarm):
    print("You should see your webpage now:==")
    wb.open(url)
