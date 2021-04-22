name = input("Please enter your name:")
id = input("Please enter your ID number:")
months = {1: 'Janauary', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August',
          9: 'September', 10: 'October', 11: 'November', 12: 'December'}
year = id[0:2]
month = id[2:4]
day = id[4:6]
citizen = id[10:11]
sex = id[6:10]
female = range(0, 4999)
male = range(5000, 9999)
if int(sex) in female:
    gender = " ,you are a female  "
else:
    gender = " ,you are a man"
x = int(month)

if int(citizen) == 1:
    status = "Non Citizen"
else:
    status = "Citizen"
print("Hello %s" % name + gender)
print("You were born on the ", day + " of : %s  " % months.get(x) + " in the year 19" + year)
print("You are a  %s" % status)
