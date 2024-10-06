import smtplib
from email.mime.text import MIMEText


def send_email_notification(machine_id, issue, email):
    msg = MIMEText(f"Issue reported for {machine_id}: {issue}")
    msg['Subject'] = f"Service Request: {machine_id}"
    msg['From'] = email
    msg['To'] = 'service_company@example.com'  # Change to the company's email

    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login('your_email@example.com', 'your_password')
        server.sendmail(email, 'service_company@example.com', msg.as_string())
    print(f"Email sent for {machine_id}")
