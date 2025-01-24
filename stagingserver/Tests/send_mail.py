import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def send_email():
    # Email configuration
    log_file_path = r"C:\Users\muduu\OneDrive\Desktop\Git chnages\Staging-automation\stagingserver\Tests\Logs\log_data.log"
    recipient_email = ["mudasir@appinessworld.com"]
    sender_email = "testingbuildingworld@gmail.com"  # Corrected typo in email
    sender_password = "fzan xsli hrvc pinh"  # App Password
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    try:
        # Create the email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = ",".join(recipient_email)
        msg['Subject'] = "Log data for the tests"

        body = ("Hello,\n\n"
                "I hope this message finds you well.\n"
                "Please find the attached log file for your reference.\n\n"
                "Best regards,\n"
                "Mohammed Mudasir A\n"
                "Software Tester")
        msg.attach(MIMEText(body, 'plain'))

        # Attach the log file
        with open(log_file_path, "rb") as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f"attachment; filename= {os.path.basename(log_file_path)}")
            msg.attach(part)

        # Send the email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()

        print("Email sent successfully!")

    except smtplib.SMTPAuthenticationError as e:
        print(f"SMTP Authentication Error: {e}")
    except FileNotFoundError:
        print(f"File not found: {log_file_path}")
    except Exception as e:
        print(f"Failed to send email: {e}")


