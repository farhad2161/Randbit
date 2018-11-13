import configparser


class BitConf:
    CONFIG_SECTION_NETWORK = "NETWORK"
    CONFIG_SECTION_NETWORK_HTTP_PROXY_URL = "HTTP_PROXY_URL"
    CONFIG_SECTION_NETWORK_HTTP_PROXY_PORT = "HTTP_PROXY_PORT"
    CONFIG_SECTION_NETWORK_API_URL = "API_SITE"

    CONFIG_SECTION_SMTP = "SMTP"
    CONFIG_SECTION_SMTP_HOST = "HOST"
    CONFIG_SECTION_SMTP_PORT = "PORT"
    CONFIG_SECTION_SMTP_USERNAME = "USERNAME"
    CONFIG_SECTION_SMTP_PASSWORD = "PASSWORD"

    CONFIG_SECTION_MAIN = "MAIN"
    CONFIG_SECTION_MAIN_THREAD_COUNT = "THREAD_COUNT"
    CONFIG_SECTION_MAIN_LOG = "LOG"

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config[self.CONFIG_SECTION_MAIN] = {
            self.CONFIG_SECTION_MAIN_THREAD_COUNT: 20,
            self.CONFIG_SECTION_MAIN_LOG: 1
        }
        self.config[self.CONFIG_SECTION_NETWORK] = {
            self.CONFIG_SECTION_NETWORK_HTTP_PROXY_URL: "",
            self.CONFIG_SECTION_NETWORK_HTTP_PROXY_PORT: 0,
            self.CONFIG_SECTION_NETWORK_API_URL: ""
        }
        self.config[self.CONFIG_SECTION_SMTP] = {
            self.CONFIG_SECTION_SMTP_HOST: "",
            self.CONFIG_SECTION_SMTP_PORT: 0,
            self.CONFIG_SECTION_SMTP_USERNAME: "",
            self.CONFIG_SECTION_SMTP_PASSWORD: ""
        }

    def load(self):
        self.config.read('config.ini')
        self.http_proxy_url = self.config[self.CONFIG_SECTION_NETWORK][self.CONFIG_SECTION_NETWORK_HTTP_PROXY_URL]
        self.http_proxy_port = self.config[self.CONFIG_SECTION_NETWORK][self.CONFIG_SECTION_NETWORK_HTTP_PROXY_PORT]
        self.api_url = self.config[self.CONFIG_SECTION_NETWORK][self.CONFIG_SECTION_NETWORK_API_URL]
        self.smtp_host = self.config[self.CONFIG_SECTION_SMTP][self.CONFIG_SECTION_SMTP_HOST]
        self.smtp_port = self.config[self.CONFIG_SECTION_SMTP][self.CONFIG_SECTION_SMTP_PORT]
        self.smtp_username = self.config[self.CONFIG_SECTION_SMTP][self.CONFIG_SECTION_SMTP_USERNAME]
        self.smtp_password = self.config[self.CONFIG_SECTION_SMTP][self.CONFIG_SECTION_SMTP_PASSWORD]
        self.thread_count = int(self.config[self.CONFIG_SECTION_MAIN]
                                [self.CONFIG_SECTION_MAIN_THREAD_COUNT])
        self.log = int(
            self.config[self.CONFIG_SECTION_MAIN][self.CONFIG_SECTION_MAIN_LOG])
