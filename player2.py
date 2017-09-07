#! /usr/bin/python3
import smtplib
s = smtplib.SMTP('smtp.gmail.com',587)
s.starttls() 
s.login("nikhiln559@gmail.com","navyachandrika37")
message ="Message_you_need_send"
s.sendmail("nikhiln559@gamil.com","nikhiln559@gmail.com",message)
s.quit()

