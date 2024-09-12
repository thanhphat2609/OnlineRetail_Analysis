class mail_alert:
    def __init__(self) -> None:
        # Email Credentials
        self.HOST = "smtp-mail.outlook.com"
        self.PORT = 587

        self.FROM_EMAIL = "20520270@ms.uit.edu.vn"

    # Email content
    def send_email(self, body, to_email, password) -> None:

        """
            Function for sending mail to alert quality check

            Args:
                body:
                to_email:
                password:
            
            Return: None
        
        """

        import smtplib

        smtp = smtplib.SMTP(self.HOST, self.PORT)

        status_code, response = smtp.ehlo()
        # print(f"[*] Echoing the server: {status_code} {response}")

        status_code, response = smtp.starttls()
        # print(f"[*] Starting TLS connection: {status_code} {response}")

        status_code, response = smtp.login(self.FROM_EMAIL, password)
        # print(f"[*] Logging in: {status_code} {response}")

        try:
            smtp.sendmail(self.FROM_EMAIL, to_email, body)
            # print("Send mail Successfully!!!")
        except Exception as e:
            print("Send mail Failed: ", e)
        else:
            smtp.quit()
