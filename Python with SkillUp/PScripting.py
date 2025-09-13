import os
import time
import smtplib

#using os module

def current_directory():
    path = os.getcwd()
    print(path)


def file_path(filename):
    path1 = os.path.abspath((filename))
    print(path1)

filename = "geek.exe"
file_path(filename)


#using time module
epc = time.time()
localtime = time.localtime(epc)
print(localtime)

#using smtplib module
smtp_obj =smtplib.SMTP('smtp.gmail.com', 587)
smtp_obj.ehlo()
smtp_obj.starttls()
smtp_obj.login('HerbertBuilds@gmail.com','Triumph8-Gentile4-Mounted4-Screen4-Prompter6')
smtp_obj.sendmail("HerbertBuilds@gmail.com", "jantjiesherbert3@gmail.com", 'Subject: Test Email \n This is a test email sent from Python script')
smtp_obj.quit()
print("Email sent successfully!")

