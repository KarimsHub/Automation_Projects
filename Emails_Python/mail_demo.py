import imghdr
import smtplib
from email.message import EmailMessage

EMAIL_ADRESS = 'example@gmail.com' # insert your mailadress in string format
EMAIL_PASSWORD = 'example' # insert your password in string format

contacts = ['example@gmail.com', 'example@gmail.com'] # insert mutiple Mailadresses

msg = EmailMessage()
msg['Subject'] = 'Gemeinsames Essen dieses Wochenende?' # insert the subject of the mail
msg['From'] = EMAIL_ADRESS
msg['To'] = contacts
msg.set_content('Wie wäre es am Samstag um 18 Uhr?') # insert the content of the mail

#Attching pictures
#files = ['example.png'] # if you like to attach more than one file to the mail just add to the list. Files have to be in the same directory as the script
#
#for file in files: # loop iterating through every file
#    with open (file, 'rb') as f:
#        file_data = f.read()
#        file_type = imghdr.what(f.name)
#        file_name = f.name
#
#    msg.add_attachment(file_data, maintype = 'image', subtype = file_type, filename = file_name) # attaches 

#Attaching PDF Files
files = ['example.pdf', 'example.png'] # if you like to attach more than one file to the mail just add to the list. Files have to be in the same directory as the script

for file in files: # loop iterating through every file
    with open (file, 'rb') as f:
        file_data = f.read()
        file_name = f.name

    msg.add_attachment(file_data, maintype = 'application', subtype = 'octet-stream', filename = file_name) # attaches 

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADRESSE, EMAIL_PASSWORT)

    smtp.send_message(msg)