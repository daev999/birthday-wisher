##################### Hard Starting Project ######################
import datetime as dt
import pandas

now = dt.datetime.now()

today_month = now.month
today_day = now.day

birthdays = pandas.read_csv("birthdays.csv")

for index, row in birthdays.iterrows():
    pass

# 1. Update the birthdays.csv with your friends & family's details.
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

# Goal
# │
# └── Send a birthday email automatically.
#
# ────────────────────────────
#
# Information
#
# • Today's month and day
# • Birthday list
# • Names
# • Email addresses
# • Birthday letter templates
#
# ────────────────────────────
#
# Decision
#
# Is today someone's birthday?
#
#         │
#    No ──┘ End
#
#         │
#        Yes
#
# ────────────────────────────
#
# Actions
#
# • Pick a random letter
# • Replace [NAME]
# • Create the email
# • Connect to Gmail
# • Log in
# • Send the email
# • End

