import smtplib
from ssl import _PasswordType

my_email = "shree@gmail.com"
password = "llihcorv"
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="newuser@gmail.com",
        msg="Subject:Hello\n\nThis is body of mail..!!"
    )


