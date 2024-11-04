import smtpd, ssl
import smtplib

def send_email(recipient, email):
    port = 465
    smtp_server = "smtp.gmail.com"
    sender = "oskarswat6@gmail.com"
    password = "zyprzdgvmadbcsxu"

    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as smtp:
            smtp.login(sender, password)
            smtp.sendmail(sender, recipient, email)
        print("Email sent successfully")
    except Exception as e:
        print(f"An error occurred: {e}")
