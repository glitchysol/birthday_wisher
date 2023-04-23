import smtplib
import datetime as dt
import random
import pandas


my_email = "YOUR EMAIL HERE"
password = "YOUR EMAIL PASSWORD"

# 1. Update the birthdays.csv. Insert names, emails, and birthdays of people you wish to say happy birthday to.
birthdays = {
    "name": ["Mom", "Dad", "Sister", "Brother", "Dev"],
    "email": ["_@yahoo.com", "_@yahoo.com",
              "_@gmail.com", "_@yahoo.com", "_@gmail.com"],
    "year": [1970, 1969, 1996, 1998, 1996],
    "month": [9, 10, 12, 3, 1],
    "day": [28, 27, 20, 24, 19]
}
df = pandas.DataFrame(birthdays)

# Append existing csv below

# df.to_csv("birthdays.csv", mode="a", index=False, header=False)

# 2. Check if today matches a birthday in the birthdays.csv
all_birthdays = pandas.read_csv("birthdays.csv")
now = dt.datetime.now()
bday_dict = all_birthdays.to_dict("records")
print(bday_dict)
name = ""
replace = "[NAME]"
bday_email = ""
for person in bday_dict:
    if person["month"] == now.month and person["day"] == now.day:
        name = person["name"]
        bday_email = person["email"]
# 3. If step 2 is true, pick a random letter from letter templates
# and replace the [NAME] with the person's actual name from birthdays.csv
letter_num = random.randint(1, 3)
with open(f"letter_templates/letter_{letter_num}.txt") as letter:
    temp_letter = letter.read()
bday_letter = temp_letter.replace(replace, name)
with open(f"hbd_{name}.txt", "w") as file:
    file.write(bday_letter)
# 4. Send the letter generated in step 3 to that person's email address.
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs=bday_email,
                        msg=f"Subject:Happy Birthday\n\n{bday_letter}")
