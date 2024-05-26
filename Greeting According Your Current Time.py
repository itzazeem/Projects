import time

time1=time.strftime('%H:%M')
# time=today.time()
print(time.strftime('%I:%M:%S%p').replace('AM', 'am').replace('PM', 'pm'),sep=':',end=" ")
 
if(time1>='00:00' and time1<='11:59'):
  print("Good Morning")
elif(time1>='12:00' and time1<='15:59'):
  print("Good Afternoon")
elif(time1>='16:00' and time1<='19:59'):
  print("Good Evening")
elif(time1>='20:00' and time1<='23:59'):
  print("Good Night")
