import smtplib
from email.mime.text import MIMEText

def send_email_alert(user_email, message_body):
    msg = MIMEText(message_body)
    msg['Subject'] = 'Low Balance Alert'
    msg['From'] = 'no-reply@fintechapp.com'
    msg['To'] = user_email

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login('your-email@gmail.com', 'your-email-password')
        server.sendmail(msg['From'], [msg['To']], msg.as_string())
