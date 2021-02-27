import datetime

print("What do you want to do")
print("1. Find todays date and time ")
print("2. Find the diff. of days between two dates ")
print("3. Find the days you have lived ")
ans = input("Answer : ")
if(ans == '1'):
  today = datetime.datetime.today()
  print(today)
elif(ans == '2'):
  y1 = int(input("Enter year1 : "))
  m1 = int(input("Enter month1 : "))
  d1 = int(input("Enter date1 : "))
  y2 = int(input("Enter year2 : "))
  m2 = int(input("Enter month2 : "))
  d2 = int(input("Enter date2 : "))
  dd1 = datetime.date(y1, m1, d1)
  dd2 = datetime.date(y2, m2, d2)
  dif = (dd2-dd1).days
  print(dif)
elif(ans == '3')
  y3 = int(input("Enter birth year : "))
  m3 = int(input("Enter birth month : "))
  d3 = int(input("Enter birth date : "))
  bd = datetime.date(y3, m3, d3)
  tod = datetime.date.today()
  diff = (tod-bd).days
  print(diff)
else:
  print("Please input 1,2,3 in the answer")
