from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from smtplib import SMTPException
def send_mail(username,email):
    msg = MIMEMultipart()  # create a message
    msg['From'] = "dgharshitha@gmail.com"
    msg['To'] = email
    msg['Subject'] = "Sports Club Registration Confirmation"
    body = f"Hi {username},\n Your request for booking the slot has been processed successfully.\nNOTE:Kindly do the payment to the link that will be shared by our Executive at the Sports Club."
    msg.attach(MIMEText(body, 'plain'))
    text = msg.as_string()
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("dgharshitha@gmail.com", "harshi9481087082")
    # Sending the mail
    try:
        s.sendmail(msg['From'], msg['To'], text)
        # Terminating the session
        s.quit()
        return True
        #raise smtplib.SMTPRecipientsRefused
    except smtplib.SMTPRecipientsRefused as e:
        return False