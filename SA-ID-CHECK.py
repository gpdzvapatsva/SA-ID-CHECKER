from datetime import date
name = input("Please enter your name:")  # Enter the user name
id = input("Please enter your ID number:") # Enter user ID Number
# Use a dictionary to store months (key and values)
months = {1: 'Janauary', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August',
          9: 'September', 10: 'October', 11: 'November', 12: 'December'}
# Use lists to extract year, month, day, citizen status, gender
year = id[0:2]
month = id[2:4]
day = id[4:6]
citizen = id[10:11]
sex = id[6:10]
# set range values for female and male
female = range(0, 4999)
male = range(5000, 9999)
# Use an if statement to check gender status
if int(sex) in range(0, 4999):
    gender = " ,you are a female  "
elif int(sex) in range(5000, 9999):
    gender = " ,you are a man"
else:
    print("Gender not recognised")
x = int(month)

if int(citizen) == 1:
    status = "Non Citizen"
else:
    status = "Citizen"
print("Hello %s" % name + gender)
print("You were born on the ", day + " of : %s  " % months.get(x) + " in the year 19" + year)
print("You are a  %s" % status)
today=date.today()
print("The date is %s" % today)
