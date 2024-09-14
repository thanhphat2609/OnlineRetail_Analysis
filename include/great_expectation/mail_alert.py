class mail_alert:
    def __init__(self) -> None:
        # Email Credentials
        self.HOST = "smtp-mail.outlook.com"
        self.PORT = 587

        self.FROM_EMAIL = "20520270@ms.uit.edu.vn"

    # Email content
    def send_email(self, subject,  body, to_email, password) -> None:
        """
        Function for sending mail to alert quality check

        Args:
            subject: The subject of the email
            body: The HTML body of the email
            to_email: Recipient email address
            password: Sender's email account password
        
        Return: None
        """
        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText

        # Create the SMTP connection
        smtp = smtplib.SMTP(self.HOST, self.PORT)

        status_code, response = smtp.ehlo()
        # Start TLS for secure connection
        status_code, response = smtp.starttls()

        # Login to the SMTP server
        status_code, response = smtp.login(self.FROM_EMAIL, password)

        # Prepare the email message
        message = MIMEMultipart("alternative")
        message['Subject'] = subject
        message['From'] = self.FROM_EMAIL
        message['To'] = to_email

        # Attach the HTML body
        html_part = MIMEText(body, 'html')
        message.attach(html_part)

        try:
            # Send the email
            smtp.sendmail(self.FROM_EMAIL, to_email, message.as_string())
            # print("Send mail Successfully!!!")
        except Exception as e:
            print("Send mail Failed: ", e)
        finally:
            smtp.quit()

