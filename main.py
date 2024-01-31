##################### Extra Hard Starting Project ######################
import pandas as pd
import random, os
import smtplib
import datetime as dt

gmail_pass = "x"
my_email = "x"

# 1. Update the birthdays.csv
birthday_list = pd.read_csv("birthdays.csv")
birthdays = birthday_list.iloc[0]['email']
day = dt.datetime.now()
today = day.day
month = day.month
print(today, month)


for i in range(len(birthday_list)):
    if birthday_list.iloc[i]['month'] == month and birthday_list.iloc[i]['day'] == today:

        letter = random.choice(os.listdir('letter_templates'))
        with open(f"letter_templates/{letter}", 'r') as bday_file:
            birthday_letter = bday_file.read()
            # (birthday_letter.replace("[NAME]", birthday_list.iloc[i]['name']))
            bday_message = birthday_letter.replace("[NAME]", birthday_list.iloc[i]['name'])
        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(my_email, gmail_pass)
            connection.sendmail(from_addr=my_email, to_addrs="dariusid08@gmail.com", msg=f"Subject:Happy Birthday!!\n\n"
                                                                                         f"{bday_message}")

