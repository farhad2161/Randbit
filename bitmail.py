import smtplib


class BitMail:
    @staticmethod
    def send_email(message):
        server = smtplib.SMTP_SSL('elapsica.com', 465)
        server.login("admin@farhadkia.ir", "niQA3iy!UFRg")
        server.sendmail(
            "admin@farhadkia.ir",
            "farhad2161@gmail.com",
            "[randbit]"+message)
        server.quit()
