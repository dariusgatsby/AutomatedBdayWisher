##################### Extra Hard Starting Project ######################
import pandas as pd
import random, os
import smtplib
import datetime as dt
import letter_templates

# 1. Update the birthdays.csv
birthday_list = pd.read_csv("birthdays.csv")
birthdays = birthday_list.iloc[0]['email']
day = dt.datetime.now()
today = day.day
month = day.month
print(today, month)

# 2. Check if today matches a birthday in the birthdays.csv
for i in range(len(birthday_list)):
    if birthday_list.iloc[i]['month'] == month and birthday_list.iloc[i]['day'] == today:
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv
        letter = random.choice(os.listdir('letter_templates'))
        with open()
# 4. Send the letter generated in step 3 to that person's email address.
