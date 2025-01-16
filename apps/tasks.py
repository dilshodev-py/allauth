import smtplib, ssl

from AllAuth.settings import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(receiver_email , url):

    sender_email = EMAIL_HOST_USER
    password = EMAIL_HOST_PASSWORD

    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message

    html = f"""
    <html>
      <body>
        <p>Hi,<br>
           How are you?<br>
           <h5>{url}</h5> 
           has many great tutorials.
        </p>
      </body>
    </html>
    """

    part2 = MIMEText(html, "html")
    message.attach(part2)
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )