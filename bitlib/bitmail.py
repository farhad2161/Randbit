import smtplib


class BitMail:
    smtp_host = ""
    smtp_port = 0
    smtp_username = ""
    smtp_password = ""

    def __init__(self, smtp_host, smtp_port, smtp_username, smtp_password):
        self.smtp_host = smtp_host
        self.smtp_port = smtp_port
        self.smtp_username = smtp_username
        self.smtp_password = smtp_password

    def send_email(self, message):
        server = smtplib.SMTP_SSL(self.smtp_host, self.smtp_port)
        server.login(self.smtp_username, self.smtp_password)
        server.sendmail(
            "admin@farhadkia.ir",
            "farhad2161@gmail.com",
            "[randbit]"+message)
        server.quit()
