import re
import datetime


password_reqs = re.compile(r"^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=!]).*$")
email_reqs = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
now = datetime.datetime.now()
save_date = now.strftime("%d.%m.%Y")
save_time = now.strftime("%H_%M_%S")

while True:
    email_ = input("Enter your email (example@gmail.com): ")
    if not email_reqs.search(email_):
        print("Mail must be followed requirements!")
        continue
    password = input("Your password: ")
    if not password_reqs.search(password):
        print("Password must be followed requirements: lengths: 8 or more, chars at least: one number, one special "
              "symbol(@#$%^&+=!), one capital letter and one lowercase letter")
        continue
    with open(f"saved_from_{save_date}.{save_time}.txt", "w") as write_file:
        write_file.write(f"Email: {email_}\nPassword: {password}")
        print("Email and password successfully saved!")
        break
input("Enter something to quit: ")
