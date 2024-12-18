import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email credentials
sender_email = "yourname@domain.com"
receiver_email = "reciever@domain.com"
password = "password"  # Use an app password if 2FA is enabled.

# Email content
subject = "Test Email"
body = """
Hello,

This is a test email sent using Python!

Best regards,
Your Python Script
"""

# Create the email
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

# Send the email
try:
    # Connect to the Gmail SMTP server
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()  # Secure the connection
        server.login(sender_email, password)  # Login to your account
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")
