import smtplib

my_email = "shree@gmail.com"
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()