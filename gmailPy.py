import smtplib, ssl
from reader import sendInfo
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

info = sendInfo()
sender_email = "briannwenn@gmail.com"
receiver_email = "julieanreb@yahoo.com"
password = "diuuvkfluezeizgs"


message = MIMEMultipart("alternative")
message["Subject"] = f"Brian Hours {info.subjectString}"
message["From"] = sender_email
message["To"] = receiver_email

# Create the plain-text and HTML version of your message
text = f"""\
Hey Julie, these are my hours worked from {info.dateRangeStr}

{sum(info.hoursWorked)} hours total."""
html = f"""\
<html>
  <body>
    <p style="color: black">Hi Julie, these are my hours worked from {info.dateRangeStr}</p>
        <table style="border: 1px solid black; border-collapse: collapse;">
            <tr>
                <th style="border: 1px solid black; border-collapse: collapse;">Date</th>
                <th style="border: 1px solid black; border-collapse: collapse;">Hours</th>
                <th style="border: 1px solid black; border-collapse: collapse;">Time</th>
                <th style="border: 1px solid black; border-collapse: collapse;">Location</th>
            </tr>
            {info.tableString}
        </table>
        <p style="color: black">{sum(info.hoursWorked)} hours total.</p>
  </body>
</html>
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2) 


context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())