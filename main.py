##################### Hard Starting Project ######################
import datetime as dt
import pandas
import random
import smtplib
from email.message import EmailMessage


now = dt.datetime.now()

today_month = now.month
today_day = now.day
birthdays = pandas.read_csv("birthdays.csv")

birthdays_dict = {}

MY_EMAIL = "your_email"
MY_PASSWORD = "your_password"

for index, row in birthdays.iterrows():
    birthdays_dict[row["month"], row["day"]] = row

if (today_month, today_day) in birthdays_dict:
    celebrant = birthdays_dict[(today_month, today_day)]
    letters = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]
    chosen_letter = random.choice(letters)
    with open (chosen_letter, "r") as file:
        letter = file.read()
        letter = letter.replace("[NAME]", celebrant["name"])

    message = EmailMessage()
    message["Subject"] = "Happy Birthday!"
    message["From"] = MY_EMAIL
    message["To"] = celebrant["email"]
    message.set_content(letter)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.send_message(message)
