import requests
import time


class BitNet:
    proxy = dict()
    error_count = 0
    MAX_ERROR_COUNT = 15

    def __init__(self, api_url, http_proxu_url, http_proxy_port):
        self.api_url = api_url
        self.session = requests.Session()
        if http_proxu_url:
            self.proxy = dict(http=http_proxu_url + ":" + http_proxy_port,
                              https=http_proxu_url + ":" + http_proxy_port)

    def get_balance(self, address):
        try:
            if self.error_count > 0:
                self.error_count -= 1

            if self.api_url == "blockchain.info":
                result = self.get_balance_blockchain_info(address)
            elif self.api_url == "blockcypher.com":
                result = self.get_balance_blockcypher_com(address)
            elif self.api_url == "blockexplorer.com":
                result = self.get_balance_blockexplorer_com(address)
            elif self.api_url == "btc.com":
                result = self.get_balance_btc_com(address)
            else:
                result = self.get_balance_bitaps_com(address)

            if result.isdigit() == False:
                raise Exception("NOT A NUMBER")

            return result
        except Exception as e:
            print(str(e))
            self.error_count += 2

            time.sleep(1)

            if self.error_count > self.MAX_ERROR_COUNT:
                self.error_count = 0
                time.sleep(10)
                return "0"

            return self.get_balance(address)

    def get_balance_blockchain_info(self, address):
        r = self.session.get(
            "https://blockchain.info/q/addressbalance/" + address, proxies=self.proxy)

        return r.text

    def get_balance_bitaps_com(self, address):
        r = self.session.get("https://bitaps.com/api/address/" +
                             address, proxies=self.proxy)

        return str(r.json()['balance'])

    def get_balance_blockexplorer_com(self, address):
        r = self.session.get(
            "https://blockexplorer.com/api/addr/{}/balance".format(address), proxies=self.proxy)

        return r.text

    def get_balance_btc_com(self, address):
        r = self.session.get(
            "https://chain.api.btc.com/v3/address/" + address, proxies=self.proxy)

        r = r.json()
        if r['data'] == None:
            return "0"

        return r['data']['balance']

    def get_balance_blockcypher_com(self, address):
        r = self.session.get(
            "https://api.blockcypher.com/v1/btc/main/addrs/" + address + "/balance", proxies=self.proxy)

        return str(r.json()['balance'])
