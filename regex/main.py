import re
import datetime


password_reqs = r"^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=!]).*$"
email_reqs = r"^[a-z0-9]+[\._]?[ a-z0-9]+[@]\w+[. ]\w{2,3}$"
save_date = datetime.datetime.now().strftime("%d.%m.%Y")
save_time = datetime.datetime.now().strftime("%H_%M_%S")

while True:
    email_ = input("Enter your email (example@gmail.com): ")
    if not re.search(email_reqs, email_):
        print("Mail must be followed requirements!")
        continue
    password = input("Your password: ")
    if not re.search(password_reqs, password):
        print("Password must be followed requirements: lengths: 8 or more, chars at least: one number, one special "
              "symbol(@#$%^&+=!), one capital letter and one lowercase letter")
        continue
    with open(f"saved_from_{save_date}.{save_time}.txt", "w") as write_file:
        write_file.write(f"Email: {email_}\nPassword: {password}")
        print("Email and password successfully saved!")
        break
input("Enter something to quit: ")
