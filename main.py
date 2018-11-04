import threading
import bitlib
import configparser

CONFIG_SECTION_NETWORK = "NETWORK"
CONFIG_SECTION_NETWORK_HTTP_PROXY_URL = "HTTP_PROXY_URL"
CONFIG_SECTION_NETWORK_HTTP_PROXY_PORT = "HTTP_PROXY_PORT"

CONFIG_SECTION_SMTP = "SMTP"
CONFIG_SECTION_SMTP_HOST = "HOST"
CONFIG_SECTION_SMTP_PORT = "PORT"
CONFIG_SECTION_SMTP_USERNAME = "USERNAME"
CONFIG_SECTION_SMTP_PASSWORD = "PASSWORD"

CONFIG_SECTION_THREAD = "THREAD"
CONFIG_SECTION_THREAD_COUNT = "COUNT"

bitmail = None
bitnet = None


def run(name):
    print("{} started!".format(name))

    while True:
        private_key = bitlib.BitGen.generate_private_key()
        wif = bitlib.BitGen.private2wif(private_key)
        address = bitlib.BitGen.private2address(private_key)
        balance = bitnet.get_balance(address)
        print("private:{},wif:{},address:{},balance:{}".format(
            private_key, wif, address, balance))

        if balance.isdigit() == False:
            print(balance)
            continue

        if balance != "0":
            f = open("success.txt", "a")
            message = private_key+"\n"+wif+"\n"+address+"\n"+balance+"\n"
            f.write(message)
            f.close()
            bitmail.send_email(message)


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config[CONFIG_SECTION_THREAD] = {
        CONFIG_SECTION_THREAD_COUNT: 20
    }
    config[CONFIG_SECTION_NETWORK] = {
        CONFIG_SECTION_NETWORK_HTTP_PROXY_URL: "",
        CONFIG_SECTION_NETWORK_HTTP_PROXY_PORT: 0
    }
    config[CONFIG_SECTION_SMTP] = {
        CONFIG_SECTION_SMTP_HOST: "",
        CONFIG_SECTION_SMTP_PORT: 0,
        CONFIG_SECTION_SMTP_USERNAME: "",
        CONFIG_SECTION_SMTP_PASSWORD: ""
    }

    config.read('config.ini')
    http_proxy_url = config[CONFIG_SECTION_NETWORK][CONFIG_SECTION_NETWORK_HTTP_PROXY_URL]
    http_proxy_port = config[CONFIG_SECTION_NETWORK][CONFIG_SECTION_NETWORK_HTTP_PROXY_PORT]
    smtp_host = config[CONFIG_SECTION_SMTP][CONFIG_SECTION_SMTP_HOST]
    smtp_port = config[CONFIG_SECTION_SMTP][CONFIG_SECTION_SMTP_PORT]
    smtp_username = config[CONFIG_SECTION_SMTP][CONFIG_SECTION_SMTP_USERNAME]
    smtp_password = config[CONFIG_SECTION_SMTP][CONFIG_SECTION_SMTP_PASSWORD]
    thread_count = int(config[CONFIG_SECTION_THREAD]
                       [CONFIG_SECTION_THREAD_COUNT])

    bitmail = bitlib.BitMail(smtp_host, smtp_port,
                             smtp_username, smtp_password)
    bitnet = bitlib.BitNet(http_proxy_url, http_proxy_port)

    # bitmail.send_email("I am runing")
    for x in range(thread_count):
        thread_name = "Thread-{}".format(x + 1)
        mythread = threading.Thread(target=run, args=(thread_name,))
        mythread.start()
