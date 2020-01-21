import os
import smtplib
from email.mime.text import MIMEText

class bcolors:
	OKGREEN = '\033[92m'
	ENDC = '\033[0m'

def fblg():
	print(bcolors.OKGREEN + '''
	$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
	$$$$$$$$_________$$$$____________$$$$_________$$$$___$$$$___$$$$$$$$$$$
	$$$$$$$$__$$$$$$$$$$$__$$$__$$$__$$$$__$$$$$__$$$$___$$$$___$$$$$$$$$$$
	$$$$$$$$__$$$$$$$$$$$__$$$__$$$__$$$$__$$$$$__$$$$___$$$$___$$$$$$$$$$$
	$$$$$$$$_________$$$$__$$$__$$$__$$$$_________$$$$___$$$$___$$$$$$$$$$$
	$$$$$$$$__$$$$$$$$$$$__$$$__$$$__$$$$__$$$$$__$$$$___$$$$___$$$$$$$$$$$
	$$$$$$$$__$$$$$$$$$$$__$$$__$$$__$$$$__$$$$$__$$$$___$$$$___$$$$$$$$$$$
	$$$$$$$$_________$$$$__$$$__$$$__$$$$__$$$$$__$$$$___$$$$__________$$$$
	$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
	''' + bcolors.ENDC)

def mailMessage(sender, recipient):
    """ Send Mail Message to Specific Recipient Without Attachment """

    msg = MIMEText('Disk space in your server is running slow (less than 10% free)')
    msg['Subject'] = 'Service Down'
    msg['From'] = sender
    msg['To'] = recipient
    # print(msg.as_string())
    mail = smtplib.SMTP('smtp.sendgrid.net', 587)
    mail.login('username', 'password')
    mail.sendmail(sender, recipient, msg.as_string())


if __name__ == "__main__":

    print('\nStart Sending Your Email .. Please Wait !!\n')
    # mailMessage('test@example.com', 'abdelrhman.hassan@rootgate.com')
    fblg()
    print('\nYour Email Has Been Sent To Your Destination :) \n')


