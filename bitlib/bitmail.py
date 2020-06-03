import smtplib


class BitMail:

    def __init__(self, smtp_host, smtp_port, smtp_username, smtp_password, mail_from, mail_to):
        self.smtp_host = smtp_host
        self.smtp_port = smtp_port
        self.smtp_username = smtp_username
        self.smtp_password = smtp_password
        self.mail_from = mail_from
        self.mail_to = mail_to

    def send_email(self, subject, message):
        if not self.smtp_host:
            return

        message = "Subject: [randbit]{}\n\n{}".format(subject, message)
        server = smtplib.SMTP_SSL(self.smtp_host, self.smtp_port)
        server.login(self.smtp_username, self.smtp_password)
        server.sendmail(self.mail_from, self.mail_to, message)
        server.quit()
